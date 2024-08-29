from utils import FindUser , ReplyWithException, ToMoney, StripMention, IsValidMention
from econ.cards.cards import cards , FindCardIndex
import discord
import singletons

async def DisplayBalance(message : discord.Message, command : list[str]) -> None:
    """Displays the balance of the user."""
   # await message.reply("DisplayBalance Command Invoked!") # Uncomment when debugging.

    # If no user is mentioned, then the balance of the user who invoked the command is displayed.
    if len(command) == 1:
        view = None
        user = FindUser(uid=message.author.id, sid=message.guild.id) # Find the user who invoked the command.

        if user.bank_acc.IsCardMaxxed():
            view = CardView(original_user=message.author, message=message)
        
        embed = await GetEmbedBalance(user=user)
        await message.reply(embed=embed, view=view)
        return
    
    if await IsValidMention(command[1]):
        mentioned_user_id = StripMention(command[1])
    else:
        await ReplyWithException(message=message, exception_msg="Invalid user!")
        return
        
    # Display the balance of the mentioned user.
    mentioned_user = FindUser(uid=mentioned_user_id, sid=message.guild.id)
    embed = await GetEmbedBalance(user=mentioned_user)
    await message.reply(embed=embed)

async def GetEmbedBalance(user) -> discord.Embed:
    """Returns an Embed with the User's Balance."""
    message_author = await singletons.client.fetch_user(user.uid)

    embed = discord.Embed(title=f"{message_author.display_name}",color=discord.Color.dark_green())
    embed.set_thumbnail(url=message_author.display_avatar.url)
    embed.set_image(url=user.bank_acc.bank_card.GetCardImage())

    embed.add_field(name="Cash:",value=f"{ToMoney(user.bank_acc.GetCashOnHand())}")
    embed.add_field(name="Bank:",value=f"{ToMoney(user.bank_acc.GetDeposit())}")
    embed.add_field(name=user.bank_acc.bank_card.GetCardName(), value=f"Max -> {ToMoney(user.bank_acc.bank_card.GetCardMax())}", inline=False)

    embed.set_footer(text=f"Networth: {ToMoney(user.GetNetWorth())}")

    return embed


class CardView(discord.ui.View):

    def __init__(self, original_user, message, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.message = message
        
    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id

    @discord.ui.button(label="Upgrade Card!", style=discord.ButtonStyle.green)
    async def UpgradeCard(self, interaction: discord.Interaction, button: discord.ui.Button):
        """Upgrades the card."""
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        user = FindUser(uid=self.original_user.id, sid=self.message.guild.id)

        if user.bank_acc.GetDeposit() >= user.bank_acc.bank_card.GetCardMax():

            next_card_index = FindCardIndex(user.bank_acc.bank_card) + 1 # Gets the next card index.
        
            user.bank_acc.bank_card = cards[next_card_index]
            user.bank_acc.SetDeposit(newdep=0.0)

            embed = await GetEmbedBalance(user=user)
            await interaction.response.edit_message(embed=embed, view=None)

