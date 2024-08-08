import singletons
import discord
import utils

async def Balance(message : discord.Message, command : list[str]) -> None:
    """Displays the balance of the user."""
   # await message.reply("Balance Command Invoked!") # Uncomment when debugging.

    # If no user is mentioned, then the balance of the user who invoked the command is displayed.
    if len(command) == 1:
        user = utils.FindUser(uid=message.author.id, sid=message.guild.id) # Find the user who invoked the command.

        embed = await utils.GetEmbedBalance(user=user)
        await message.reply(embed=embed)
        return
    
    # Check if the user is valid.
    try:
        mentioned_user_id = int(command[1].strip("<@>"))

        await singletons.client.fetch_user(mentioned_user_id)
    except:
        await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
        return
    
    mentioned_user_id = int(command[1].strip("<@>"))

    # Display the balance of the mentioned user.
    mentioned_user = utils.FindUser(uid=mentioned_user_id, sid=message.guild.id)
    embed = await utils.GetEmbedBalance(user=mentioned_user)

    await message.reply(embed=embed)

async def Withdraw(message : discord.Message, command : list[str]) -> None:
    """Withdraws money from the bank account."""
    # await message.reply("Withdraw Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if len(command) == 1:
        if user.bank_acc.GetDeposit() == 0.0:
            await utils.ReplyWithException(message=message, exception_msg="You have no money to withdraw.")
            return
        embed = discord.Embed(title=f"Succesfully withdrawn {user.bank_acc.GetDeposit():,.2f}",color=discord.Color.green())

        user.bank_acc.WithdrawAmount(user.bank_acc.GetDeposit())

        await message.reply(embed=embed)
        return
    
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            await utils.ReplyWithException(message=message, exception_msg="Invalid funds provided.")
            return
        
        funds = float(command[1])

        if user.bank_acc.GetDeposit() >= funds and funds > 0.00:
            user.bank_acc.WithdrawAmount(funds)
            embed = discord.Embed(title=f"Succesfully withdrawn {funds:,.2f}",color=discord.Color.green())
            await message.reply(embed=embed)
        else:
            await utils.ReplyWithException(message=message, exception_msg="Insufficient funds.")

async def Deposit(message : discord.Message, command : list[str]) -> None:
    """Deposits money into the bank account."""
    # await message.reply("Deposit Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if len(command) == 1:
        if user.bank_acc.GetCashOnHand() == 0.0:
            await utils.ReplyWithException(message=message,exception_msg="You have no cash on hand to deposit.")
            return
        embed = discord.Embed(title=f"Succesfully deposited {user.bank_acc.GetCashOnHand():,.2f}",color=discord.Color.green())
        user.bank_acc.DepositAmount(user.bank_acc.GetCashOnHand())
        await message.reply(embed=embed)
        return
    
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.

        try:
            float(command[1])
        except:
            await utils.ReplyWithException(message=message,exception_msg="Insufficient funds provided.")
            return
        funds = float(command[1])

        if user.bank_acc.GetCashOnHand() >= funds and funds > 0.00:
            user.bank_acc.DepositAmount(funds)
            embed = discord.Embed(title=f"Succesfully Deposited {funds:,.2f}",color=discord.Color.green())
            await message.reply(embed=embed)
        else:
            await utils.ReplyWithException(message=message,exception_msg="Insufficient funds.")
    
async def Pay(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.
    match len(command):
        case 1:
            await utils.ReplyWithException(message=message,exception_msg="Missing User and pay amount.")
            return
        
        case 2:
            await utils.ReplyWithException(message=message,exception_msg="Missing User or pay amount.")
            return
    
        case 3:
            command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
            try:
                float(command[2])
            except:
                await utils.ReplyWithException(message=message,exception_msg="Invalid funds provided.")
                return
        
    # Check if the user is valid.
    try:
        user_paid_id = int(command[1].strip("<@>"))
        await singletons.client.fetch_user(user_paid_id)
    except:
        await utils.ReplyWithException(message=message,exception_msg="User Doesnt Exist!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_paid_id = int(command[1].strip("<@>"))
    user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)

    amount = float(command[2])

    # Check if the user has enough money to pay.
    if user.bank_acc.GetCashOnHand() < amount and amount > 0.00:
        await utils.ReplyWithException(message=message,exception_msg="Insufficient funds.")
        return
    
    # Pay the user.
    user.bank_acc.RemoveCash(cash=amount)
    user_paid.bank_acc.AddCash(cash=amount)

    embed = discord.Embed(description=f"You have successfully Paid **${amount}** to <@{user_paid_id}>",color=discord.Color.green())
    await message.reply(embed=embed)