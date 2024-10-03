import singletons
import discord
import constants
import utils
import random
import asyncio
import econ.user

class RouletteGame:
    sid : int # Guild/Server ID
    bet_dict : dict[econ.user.User] # Dict with user id's as keys and their respective values as their bet amount.
    root_channel : discord.TextChannel # Channel where the roulette is being played in.
    result : int # The winning number

    def __init__(self, sid : int, root_channel : discord.TextChannel) -> None:
        self.sid = sid
        self.bet_dict = {}
        self.root_channel = root_channel
        self.result = None
    
    async def Start(self) -> None:
        roulette_task = asyncio.create_task(self.WaitRoulette())
    
    async def WaitRoulette(self) -> None:

        await self.DoWait()

        self.CalculateResult()
        self.RewardWinners()

        results = await self.GetResultsEmbed()

        singletons.active_roulettes.pop(self.sid)

        w_l = results[1] + "\n" + results[2]

        await self.root_channel.send(embed=results[0])
        await self.root_channel.send(content=w_l)

        del results
        del self
    
    async def DoWait(self) -> None:
        await asyncio.sleep(constants.ROULETTE_INTERVAL/4)
        await self.root_channel.send(embed=discord.Embed(title=f"Roulette ending in {int(constants.ROULETTE_INTERVAL - constants.ROULETTE_INTERVAL/4)} seconds"))
        await asyncio.sleep(constants.ROULETTE_INTERVAL/4)
        await self.root_channel.send(embed=discord.Embed(title=f"Roulette ending in {int(constants.ROULETTE_INTERVAL - (constants.ROULETTE_INTERVAL/2))} seconds"))
        await asyncio.sleep(constants.ROULETTE_INTERVAL/4)
        await self.root_channel.send(embed=discord.Embed(title=f"Roulette ending in {int(constants.ROULETTE_INTERVAL - (constants.ROULETTE_INTERVAL* 3/4))} seconds"))
        await asyncio.sleep(constants.ROULETTE_INTERVAL/4)

    def CalculateResult(self) -> None:
        self.result = random.randint(0, 37)
    
    def Winner(self, user : econ.user.User, multiplier : int = 1) -> None:
        self.bet_dict[user]["amount"] *= multiplier

        amount = self.bet_dict[user]["amount"]

        self.bet_dict[user]["bet"] = "WINNER" # Marks player as winner

        user.bank_acc.AddCash(amount)
    
    
    def RewardWinners(self) -> None:
        """Determines and hands out rewards to winners."""
    
        for player in self.bet_dict.keys():

            if self.bet_dict[player]["bet"] == "even" and self.result % 2 == 0:
                self.Winner(user=player)
                continue

            if self.bet_dict[player]["bet"] == "odd" and self.result % 2 != 0:
                self.Winner(user=player)
                continue
            
            if self.bet_dict[player]["bet"] == self.result:
                self.Winner(user=player, multiplier=35)
                continue

    def AppendBet(self, user : econ.user.User, amount: float, bet : str) -> bool:
        """Appends uid and their bet to the bet dict
        Returns -> Bool representing if Append was successful or not.
        """
        if user in self.bet_dict.keys(): # Fails if user already made a bet
            return False
        user.bank_acc.RemoveCash(amount)
        self.bet_dict[user] = { "amount" : amount, "bet" : bet}
        return True

    async def GetResultsEmbed(self) -> list:
        embed = discord.Embed()
        embed.title = "Roulette Ended!"
        emoji = ":black_circle:"

        if self.result % 2 != 0:
            embed.color = discord.Color.red()
            emoji = ":red_circle:"

        elif self.result == 0:
            embed.color = discord.Color.green()
            embed = ":green_circle"

        embed.add_field(name=f"Result : {self.result} {emoji}",value="")

        winner_fields = []
        loser_fields = []

        for player in self.bet_dict.keys():

            if self.bet_dict[player]["bet"] == "WINNER":
                winner = f"<@{player.uid}> WON {utils.ToMoney(self.bet_dict[player]["amount"])}"
                winner_fields.append(winner)
                continue

            loser = f"<@{player.uid}> LOST {utils.ToMoney(self.bet_dict[player]["amount"])}"
            loser_fields.append(loser)
            continue

        winner_fields = "\n".join(winner_fields)
        loser_fields = "\n".join(loser_fields)
        return [embed, winner_fields, loser_fields]
    
        
            


async def Roulette(message : discord.Message, command : list[str]) -> None:
    
    command.pop(0) # removes prefix and action

    if len(command) < 2:
        await utils.ReplyWithException(message=message, exception_msg="too little arguments given",exception_desc=f"use `{constants.PREFIX}help gambling` for more info")
        return
    
    amount = 0

    try:
        amount = int(command[0])

    except:
        await utils.ReplyWithException(message=message, exception_msg="Invalid amount",exception_desc=f"use `{constants.PREFIX}help gambling` for more info")
        return
    
    sid = message.guild.id
    user = utils.FindUser(uid=message.author.id, sid=sid)

    if user.bank_acc.GetCashOnHand() < amount:
        await utils.ReplyWithException(message=message, exception_msg="Not enough cash on hand.", exception_desc=f"You only have {utils.ToMoney(user.bank_acc.GetCashOnHand())}")
        return
        
    if amount < constants.MIN_ROULETTE_BET:
        await utils.ReplyWithException(message=message, exception_msg=f"Too low of a bet.",exception_desc=f"Minimum is {constants.MIN_BJ_BET}.")
        return

    bet = 0

    try:
        bet = int(command[1])

    except:
        match command[1].lower():
            case "red":
                bet = "odd"

            case "odd":
                bet = "odd"

            case "black":
                bet = "even"

            case "even":
                bet = "even"

            case "green":
                bet = 0
            
            case _:
                await utils.ReplyWithException(message=message, exception_msg="Not a valid bet",exception_desc="You can bet for `even, odd, red, black, green or a specific integer`")
                return
        
    if sid not in singletons.active_roulettes.keys():
        roulette = RouletteGame(sid=sid,root_channel=message.channel)
        singletons.active_roulettes[sid] = roulette
        await roulette.Start()
    else:
        roulette = singletons.active_roulettes[sid]
    
    if roulette.AppendBet(user=user, amount=amount, bet=bet):
        await message.add_reaction("✅")
        return
    
    await utils.ReplyWithException(message=message,exception_msg="You cant bet twice.",exception_desc="")
    

