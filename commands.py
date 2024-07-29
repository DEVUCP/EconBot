import discord
import os
import econessentials
import utils
import singletons
import constants
import random

async def Help(message : discord.Message) -> None:
    await message.reply(constants.HELP_MSG)

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
        await message.reply("Invalid user!")
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
        embed = discord.Embed(title=f"Succesfully withdrawn {user.bank_acc.GetDeposit():,.2f}")
        user.bank_acc.WithdrawAmount(user.bank_acc.GetDeposit())
        await message.reply(embed=embed)
        return
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            embed = discord.Embed(title="Invalid funds provided.") 
            await message.reply(embed=embed)
            return
        funds = float(command[1])
        if user.bank_acc.GetDeposit() >= funds and funds > 0.00:
            user.bank_acc.WithdrawAmount(funds)
            embed = discord.Embed(title=f"Succesfully withdrawn {funds:,.2f}")
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient funds.")  
            await message.reply(embed=embed)

async def Deposit(message : discord.Message, command : list[str]) -> None:
    """Deposits money into the bank account."""
    # await message.reply("Deposit Command Invoked!") # Uncomment when debugging.
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    if len(command) == 1:
        embed = discord.Embed(title=f"Succesfully deposited {user.bank_acc.GetCashOnHand():,.2f}")
        user.bank_acc.DepositAmount(user.bank_acc.GetCashOnHand())
        await message.reply(embed=embed)
        return
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            embed = discord.Embed(title="Invalid funds provided.") 
            await message.reply(embed=embed)
            return
        funds = float(command[1])
        if user.bank_acc.GetCashOnHand() >= funds and funds > 0.00:
            user.bank_acc.DepositAmount(funds)
            embed = discord.Embed(title=f"Succesfully Deposited {funds:,.2f}")
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient funds.")  
            await message.reply(embed=embed)
    
async def Pay(message : discord.Message, command : list[str]) -> None:
    """Pays money to another user."""
    # await message.reply("Pay Command Invoked!") # Uncomment when debugging.

    if len(command) == 1:
        embed = discord.Embed(title=f"Missing User and pay amount.")
        await message.reply(embed=embed)
        return
    if len(command) == 2:
        embed = discord.Embed(title=f"Missing User or pay amount.")
        await message.reply(embed=embed)
        return
    if len(command) == 3:
        command[2] = command[2].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[2])
        except:
            embed = discord.Embed(title="Invalid funds provided.") 
            await message.reply(embed=embed)
            return
    # Check if the user is valid.
    try:
        user_paid_id = int(command[1].strip("<@>"))
        await singletons.client.fetch_user(user_paid_id)
    except:
        await message.reply("Invalid user!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_paid_id = int(command[1].strip("<@>"))
    user_paid = utils.FindUser(uid=user_paid_id, sid=message.guild.id)

    amount = float(command[2])
    # Check if the user has enough money to pay.
    if user.bank_acc.GetCashOnHand() < amount and amount > 0.00:
        embed = discord.Embed(title="Insufficient funds.")  
        await message.reply(embed=embed)
        return
    
    # Pay the user.
    user.bank_acc.RemoveCash(cash=amount)
    user_paid.bank_acc.AddCash(cash=amount)
    paid_user = await singletons.client.fetch_user(user_paid_id)
    embed = discord.Embed(title=f"You have successfully Paid ${amount} to {paid_user.display_name}")
    await message.reply(embed=embed)

async def Work(message : discord.Message) -> None:
    """Works for money."""
    # await message.reply("Work Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    outcome = random.choice(list(constants.OUTCOMES_WORK.keys()))
    value_1, value_2 = constants.OUTCOMES_WORK[outcome]

    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")
    user.bank_acc.AddCash(cash=cash)
    
    embed = await utils.GetEmbedBalance(user=user)
    await message.reply(content=outcome.replace("#", str(cash)), embed=embed)

async def Crime(message : discord.Message) -> None:
    """Commits a crime for money."""
    # await message.reply("Crime Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    outcome = random.choice(list(constants.OUTCOMES_CRIME.keys()))
    value_1, value_2 = constants.OUTCOMES_CRIME[outcome]

    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")
    user.bank_acc.AddCash(cash=cash)

    embed = await utils.GetEmbedBalance(user=user)
    await message.reply(content=outcome.replace("#", str(cash)), embed=embed)


async def Beg(message : discord.Message) -> None:
    """Begs for money."""
    # await message.reply("Beg Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    outcome = random.choice(list(constants.OUTCOMES_BEG.keys()))
    value_1, value_2 = constants.OUTCOMES_BEG[outcome]

    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")
    user.bank_acc.AddCash(cash=cash)

    embed = await utils.GetEmbedBalance(user=user)
    await message.reply(content=outcome.replace("#", str(cash)), embed=embed)

async def Rob(message : discord.Message, command : list[str]) -> None:
    """Rob another user for money."""
    # await message.reply("Rob Command Invoked!") # Uncomment when debugging.
    
    # Check if the user is valid.
    try: 
        user_robbed_id = int(command[1].strip("<@>"))
        await singletons.client.fetch_user(user_robbed_id)
    except:
        await message.reply("Invalid user!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))
    user_robbed = utils.FindUser(uid=user_robbed_id, sid=message.guild.id)

    if user_robbed.bank_acc.cash_on_hand < 0.5:
        await message.reply("This user is too poor!")
        return
    amount = random.uniform(user_robbed.bank_acc.cash_on_hand/4, user_robbed.bank_acc.cash_on_hand/2)
    amount = float(f"{amount:,.2f}")
    # Check if the user has enough money to rob.
    
    
    # Rob the user.
    user.bank_acc.AddCash(cash=amount)
    user_robbed.bank_acc.RemoveCash(cash=amount)
    await message.reply(f"You have successfully robbed {amount} from <@{user_robbed_id}>")
