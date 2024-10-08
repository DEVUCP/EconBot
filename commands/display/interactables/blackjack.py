import discord
import constants
import utils
import random
import enum

from commands.display.interactables.interactable import interactable

class BlackJackInteractable(interactable):

    cards = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11]
    }

    class GameStatus(enum.Enum):
        ONGOING = -1
        TIE = 0
        PLAYER_WON = 1
        DEALER_WON = 2

    def __init__(self, original_user, amount, sid, timeout=280):
        super().__init__(original_user=original_user, timeout=timeout)
        self.amount = amount
        self.sid = sid
        self.dealer_hand = []
        self.player_hand = []
        self.status = self.GameStatus.ONGOING
        self.player_stood = False
        self.GenerateGame()
    
    async def on_timeout(self) -> None:
        self.Tie()
    

    # Game Ending Functions

    def Tie(self) -> None:
        self.status = self.GameStatus.TIE
        user = utils.FindUser(uid=self.original_user.id, sid=self.original_user.guild.id)
        user.bank_acc.AddCash(self.amount)
    
    def Win(self) -> None:
        self.status = self.GameStatus.PLAYER_WON
        user = utils.FindUser(uid=self.original_user.id, sid=self.original_user.guild.id)
        user.bank_acc.AddCash(self.amount * 2)
    
    def Lose(self) -> None:
        self.status = self.GameStatus.DEALER_WON


    # Card Functions

    def GenerateCard(self) -> int:
        return random.choice(list(self.cards.keys()))

    def Deal(self, hand : list[int]) -> None:
        hand.append(self.GenerateCard())

    def GenerateGame(self) -> None:
        self.dealer_hand = [self.GenerateCard()]
        self.player_hand = [self.GenerateCard(), self.GenerateCard()]
        if self.TotalHand(self.player_hand) == 21:
            self.Win()

    def TotalHand(self, hand : list[int]) -> int:

        total = 0
        for card in hand:

            if card == "A":
                continue

            total += self.cards[card]

        if "A" in hand and total + 11 <= 21:
            total += 11

        elif "A" in hand:
            total += 1

        return total

    # Player Actions

    def Stand(self) -> None:

        while self.TotalHand(self.dealer_hand) <= 16:
            self.Deal(self.dealer_hand)

        self.player_stood = True
        self.UpdateStatus()

    def Hit(self) -> None:
        self.Deal(self.player_hand)
        self.UpdateStatus()

    # Game Status Functions

    def UpdateStatus(self) -> None:

        if self.TotalHand(self.dealer_hand) > 21:
            self.Win()
            return

        if self.TotalHand(self.player_hand) > 21:
            self.Lose()
            return
        
        if len(self.player_hand) == 5:
            self.Win()
            return

        if self.TotalHand(self.player_hand) == 21:
            self.Win()
            return
        
        if self.player_stood:
            if self.TotalHand(self.player_hand) > self.TotalHand(self.dealer_hand):
                self.Win()
                return

            elif self.TotalHand(self.player_hand) < self.TotalHand(self.dealer_hand):
                self.Lose()
                return
            
            else:
                self.Tie()
                return
        

    def IsGameEnded(self) -> bool:
        return self.status != self.GameStatus.ONGOING

    @discord.ui.button(label="Stand", style=discord.ButtonStyle.green)
    async def StandButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user) or self.IsGameEnded() or self.player_stood:
            return
        
        self.Stand()
        await self.UpdateBoard(interaction=interaction)

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.blurple)
    async def HitButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user) or self.IsGameEnded() or self.player_stood:
            return

        self.Hit()
        await self.UpdateBoard(interaction=interaction)
    
    @discord.ui.button(label="Double Down", style=discord.ButtonStyle.blurple)
    async def DoubleDownButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user) or self.IsGameEnded() or self.player_stood:
            return
        

        user = utils.FindUser(uid=self.original_user.id, sid=self.sid)

        if user.bank_acc.GetCashOnHand() < self.amount * 2:
            await interaction.response.send_message("You don't have enough money to double down.")
            return

        self.amount *= 2
        user.bank_acc.RemoveCash(cash=self.amount / 2)

        self.Hit()
        await self.UpdateBoard(interaction=interaction)

 
    async def UpdateBoard(self, interaction: discord.Interaction) -> None:
        new_embed = self.CreateBoardEmbed(new=True)
        await interaction.response.edit_message(embed=new_embed)


    async def UpdateBoard(self, interaction: discord.Interaction) -> None:
        new_embed = self.CreateBoardEmbed(new=True)
        await interaction.response.edit_message(embed=new_embed)
    


    def CreateBoardEmbed(self, new : bool) -> discord.Embed:
        """Creates an embed for the Blackjack Board."""
        embed = discord.Embed(title="BlackJack")

        match self.status:

            case self.GameStatus.ONGOING:
                embed.add_field(name="Bet", value=f"{utils.ToMoney(self.amount)}", inline=False)

            case self.GameStatus.TIE:
                embed.description = "**Push!**"
                embed.add_field(name="Returned", value=f"{utils.ToMoney(self.amount)}", inline=False)
                embed.color = discord.Color.yellow()

            case self.GameStatus.PLAYER_WON:
                if self.TotalHand(self.dealer_hand) > 21:
                    embed.description = "**Dealer Bust!**"

                elif self.TotalHand(self.player_hand) == 21:
                    embed.description = "**Natural!**"

                elif len(self.player_hand) == 5:
                    embed.description = "**Five Card Charlie !**"

                else:
                    embed.description = "**Player Won!**"

                embed.add_field(name="Won", value=f"{utils.ToMoney(self.amount * 2)}", inline=False)
                embed.color = discord.Color.green()

            case self.GameStatus.DEALER_WON:

                if self.TotalHand(self.player_hand) > 21:
                    embed.description = "**Player Bust!**"

                elif self.TotalHand(self.dealer_hand) == 21:
                    embed.description = "**Natural!**"

                else:
                    embed.description = "**Dealer Won!**"

                embed.add_field(name="Lost", value=f"{utils.ToMoney(self.amount)}", inline=False)
                embed.color = discord.Color.red()

        embed.add_field(name="**Your hand**", value=f"{self.player_hand}", inline=True)
        embed.add_field(name="**Dealer's hand**", value=f"{self.dealer_hand}", inline=True)
        
        embed.add_field(name=f"",value="",inline=False) # Seperator

        player_hand_str = self.TotalHand(self.player_hand) if "A" not in self.player_hand else "Soft " + str(self.TotalHand(self.player_hand))
        dealer_hand_str = self.TotalHand(self.dealer_hand) if "A" not in self.dealer_hand else "Soft " + str(self.TotalHand(self.dealer_hand))

        embed.add_field(name=f"value: {player_hand_str}",value="",inline=True)
        embed.add_field(name=f"value: {dealer_hand_str}",value="",inline=True)

        return embed
