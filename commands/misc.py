import discord
import constants

async def Help(message : discord.Message) -> None:
    """Displays all valid commands."""
    # await message.reply("Help Command Invoked!") # Uncomment when debugging.
    
    embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())

    for command, description in constants.COMMANDS.items():
        embed.add_field(name=f"{constants.PREFIX}{command}", value=description, inline=False)

    await message.reply(embed=embed)
