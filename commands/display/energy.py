import discord
from utils import FindUser

async def DisplayEnergy(message : discord.Message) -> None:
    """Displays user's energy bar."""
    # await message.reply("Display Energy Invoked!") # Uncomment when debugging.
    
    user = FindUser(uid=message.author.id, sid=message.guild.id)
    embed = discord.Embed(title=user.energy.GetEnergyBar())
    await message.reply(embed=embed)
