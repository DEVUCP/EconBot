import discord
import utils
import saveload
from saveload import saveload

async def ManualSave(message : discord.Message) -> None:
    """Saves the user data to a file."""

    operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if not operator.op:
        await message.reply("You must be an operator to do that.")
        return
    
    await saveload.SaveUserDict()

    await message.reply("Saved!")