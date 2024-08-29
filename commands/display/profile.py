import discord
import singletons
from utils import FindUser, ReplyWithException, IsValidMention, StripMention

async def DisplayProfile(message : discord.Message, command : list[str]) -> None:
    """Displays the user's profile."""
    #await message.reply("Profile Command Invoked!") # Uncomment when debugging.

    if len(command) == 1:
        user = FindUser(uid=message.author.id, sid=message.guild.id)
        embed = await GetEmbedProfile(user=user)
    
    elif await IsValidMention(command[1]):
        mentioned_user_id = StripMention(command[1])
        user = FindUser(uid=mentioned_user_id, sid=message.guild.id)
        embed = await GetEmbedProfile(user=user)
    else:
        await ReplyWithException(message=message, exception_msg="Invalid user!")
        return

    await message.reply(embed=embed)

async def GetEmbedProfile(user) -> discord.Embed:
    """Returns an Embed with the User's Profile."""
    message_author = await singletons.client.fetch_user(user.uid)

    embed = discord.Embed(title=f"{message_author.display_name}'s Profile", description="", color=discord.Color.green())
    embed.set_thumbnail(url=message_author.avatar.url)

    embed.add_field(name="Energy", value=f"{user.energy.GetEnergyBar()}", inline=False)
    embed.add_field(name="Balance", value=f"", inline=False)
    embed.add_field(name="Cash", value=f"${user.bank_acc.GetCashOnHand():,.2f}", inline=True)
    embed.add_field(name="Deposit", value=f"${user.bank_acc.GetDeposit():,.2f}", inline=True)
    embed.add_field(name="Net Worth", value=f"${user.GetNetWorth():,.2f}", inline=True)
    embed.add_field(name="Attributes", value=f"", inline=False)

    for attribute in user.attributes:
        embed.add_field(name=attribute, value=f"{user.attributes[attribute].GetLevelPercentage():.0%}", inline=True)
    embed.add_field(name="", value=f"", inline=False)

    return embed