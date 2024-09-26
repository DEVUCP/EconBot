import discord
import utils
import singletons

async def AddOperator(message : discord.Message, command : list[str] ) -> None:
    """Adds a user to the list of operators."""
    if not message.author.guild_permissions.administrator:
        await message.reply("You must be as server administrator to do that.")
        return

    if len(command) == 1:
        new_operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if len(command) == 2:
        if await utils.IsValidMention(command[1]):
            mentioned_user_id = utils.StripMention(command[1])
        else:
            await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
            return

        new_operator = utils.FindUser(uid=mentioned_user_id, sid=message.guild.id)

    if new_operator.op:
        await message.reply("That user is already an operator.")
        return
    
    new_operator.op = True

    user = await singletons.client.fetch_user(new_operator.uid)
    
    await message.reply(f"Added {user.display_name} as an operator.")

async def RemoveOperator(message : discord.Message, command : list[str] ) -> None:
    """Removes a user from the list of operators."""
    if not message.author.guild_permissions.administrator:
        await message.reply("You must be as server administrator to do that.")
        return
    
    if len(command) == 1:
        removed_operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    if len(command) == 2:
        if await utils.IsValidMention(command[1]):
            mentioned_user_id = utils.StripMention(command[1])
        else:
            await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
            return
        removed_operator = utils.FindUser(uid=mentioned_user_id, sid=message.guild.id)

    if not removed_operator.op:
        await message.reply("That user is not an operator.")
        return
    
    removed_operator.op = False

    user = await singletons.client.fetch_user(removed_operator.uid)
    await message.reply(f"Removed {user.display_name} as an operator.")
    