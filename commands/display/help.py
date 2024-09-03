import discord
import constants

async def Help(message : discord.Message, command : list[str]) -> None:
    """Displays all valid commands."""
    # await message.reply("Help Command Invoked!") # Uncomment when debugging.
    
    if len(command) < 2:

        embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())

        for group, commands in constants.COMMANDS.items():

            for command, description in commands.items():

                if command != "description":
                    continue

                embed.add_field(name=f"{group.capitalize()} commands", value=description, inline=False)
    else:
        group = command[1].lower()

        if group not in constants.COMMANDS:

            embed = discord.Embed(title="Invalid command group, here is a list of all command groups", color=constants.EXCEPTION_COLOR)

            await message.reply(embed=embed)
            await Help(message=message, command=[]) # Calls default help command
            return

        embed = discord.Embed(title=f"{group.capitalize()} commands", color=discord.Color.blue())
        for command, description in constants.COMMANDS[group].items():
            if command != "description":
                embed.add_field(name=f"{constants.PREFIX}{command}", value=description, inline=False)

    await message.reply(embed=embed)
