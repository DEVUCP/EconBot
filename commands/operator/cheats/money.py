import discord
import utils
import singletons

async def AddCash(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.

    operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if not operator.op:
        await message.reply("You must be an operator to do that.")
        return
    
    match len(command):
        case 1:
            await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
            return
        
        case 2:
            # Diffrentiate between a user and a number.
            try:
                amount = float(command[1])
                user_paid = utils.FindUser(uid=message.author.id, sid=message.guild.id)
            except:
                try:
                    user_paid_id = utils.StripMention(command[1])
                    await singletons.client.fetch_user(user_paid_id)
                    await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
                    return   
                except:
                    await utils.ReplyWithException(message=message,exception_msg="User Doesnt Exist!")
                    return
    
        case 3:
            command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
            try:
                amount = float(command[2])
                user_paid_id = utils.StripMention(command[1])
                await singletons.client.fetch_user(user_paid_id)
                user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)
            except:
                await utils.ReplyWithException(message=message,exception_msg="Invalid funds provided or Invalid User.")
                return
    
        case _:
            await utils.ReplyWithException(message=message,exception_msg="Invalid arguments.")
            return

    disc_user = await singletons.client.fetch_user(user_paid.uid)

    # Add money to the user.
    user_paid.bank_acc.AddCash(cash=amount)

    embed = discord.Embed(description=f"You have successfully Added **${amount:,.2f}** to {disc_user.display_name}'s cash",color=discord.Color.green())
    await message.reply(embed=embed)


async def RemoveCash(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.

    operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if not operator.op:
        await message.reply("You must be an operator to do that.")
        return
    
    match len(command):
        case 1:
            await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
            return
        
        case 2:
            # Diffrentiate between a user and a number.
            try:
                amount = float(command[1])
                user_paid = utils.FindUser(uid=message.author.id, sid=message.guild.id)
            except:
                try:
                    user_paid_id = utils.StripMention(command[1])
                    await singletons.client.fetch_user(user_paid_id)
                    await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
                    return   
                except:
                    await utils.ReplyWithException(message=message,exception_msg="User Doesnt Exist!")
                    return
    
        case 3:
            command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
            try:
                amount = float(command[2])
                user_paid_id = utils.StripMention(command[1])
                await singletons.client.fetch_user(user_paid_id)
                user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)
            except:
                await utils.ReplyWithException(message=message,exception_msg="Invalid funds provided or Invalid User.")
                return
    
        case _:
            await utils.ReplyWithException(message=message,exception_msg="Invalid arguments.")
            return

    disc_user = await singletons.client.fetch_user(user_paid.uid)

    # Add money to the user.
    user_paid.bank_acc.RemoveCash(cash=amount)

    embed = discord.Embed(description=f"You have successfully Removed **${amount:,.2f}** from {disc_user.display_name}'s cash",color=discord.Color.green())
    await message.reply(embed=embed)


async def AddDeposit(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.

    operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if not operator.op:
        await message.reply("You must be an operator to do that.")
        return
    
    match len(command):
        case 1:
            await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
            return
        
        case 2:
            # Diffrentiate between a user and a number.
            try:
                amount = float(command[1])
                user_paid = utils.FindUser(uid=message.author.id, sid=message.guild.id)
            except:
                try:
                    user_paid_id = utils.StripMention(command[1])
                    await singletons.client.fetch_user(user_paid_id)
                    await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
                    return   
                except:
                    await utils.ReplyWithException(message=message,exception_msg="User Doesnt Exist!")
                    return
    
        case 3:
            command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
            try:
                amount = float(command[2])
                user_paid_id = utils.StripMention(command[1])
                await singletons.client.fetch_user(user_paid_id)
                user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)
            except:
                await utils.ReplyWithException(message=message,exception_msg="Invalid funds provided or Invalid User.")
                return
    
        case _:
            await utils.ReplyWithException(message=message,exception_msg="Invalid arguments.")
            return

    disc_user = await singletons.client.fetch_user(user_paid.uid)

    # Add money to the user.
    user_paid.bank_acc.AddDeposit(dep=amount)

    embed = discord.Embed(description=f"You have successfully Added **${amount:,.2f}** to {disc_user.display_name}'s bank account",color=discord.Color.green())
    await message.reply(embed=embed)


async def RemoveDeposit(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.

    operator = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if not operator.op:
        await message.reply("You must be an operator to do that.")
        return
    
    match len(command):
        case 1:
            await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
            return
        
        case 2:
            # Diffrentiate between a user and a number.
            try:
                amount = float(command[1])
                user_paid = utils.FindUser(uid=message.author.id, sid=message.guild.id)
            except:
                try:
                    user_paid_id = utils.StripMention(command[1])
                    await singletons.client.fetch_user(user_paid_id)
                    await utils.ReplyWithException(message=message,exception_msg="Missing funds provided.")
                    return   
                except:
                    await utils.ReplyWithException(message=message,exception_msg="User Doesnt Exist!")
                    return
    
        case 3:
            command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
            try:
                amount = float(command[2])
                user_paid_id = utils.StripMention(command[1])
                await singletons.client.fetch_user(user_paid_id)
                user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)
            except:
                await utils.ReplyWithException(message=message,exception_msg="Invalid funds provided or Invalid User.")
                return
    
        case _:
            await utils.ReplyWithException(message=message,exception_msg="Invalid arguments.")
            return

    disc_user = await singletons.client.fetch_user(user_paid.uid)

    # Add money to the user.
    user_paid.bank_acc.RemoveDeposit(dep=amount)

    embed = discord.Embed(description=f"You have successfully Removed **${amount:,.2f}** from {disc_user.display_name}'s bank account",color=discord.Color.green())
    await message.reply(embed=embed)