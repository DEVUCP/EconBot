import os
import discord
import utils
import constants

async def DisplayChangelog(message : discord.Message) -> None:
    """Displays the changelog of the bot's most recent update."""
    #await message.reply("Changelog Command Invoked!") # Uncomment when debugging.

    opened_file = open(constants.CHANGELOGS_PATH, "r")
    changelog = opened_file.read()
    opened_file.close()

    new_changelog = ""
    
    for char in changelog:

        if char == "!":
            changelog = new_changelog
            break

        new_changelog += char
    
    embed = discord.Embed(title="", description=f"Author -> https://github.com/DEVUCP \n {changelog}", color=discord.Color.dark_green())
    embed.add_field(name="", value="")
    embed.set_footer(text="If you have any questions or need any help contact the developer.")
    await message.reply(embed=embed)