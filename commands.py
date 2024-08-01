import discord
import os
import econessentials
import utils
import singletons
import constants
import random

async def Help(message : discord.Message) -> None:
    """Displays all valid commands."""
    embed = discord.Embed(title="Bot Commands", color=discord.Color.blue())
    for command, description in constants.COMMANDS.items():
        embed.add_field(name=f"{constants.PREFIX}{command}", value=description, inline=False)
    await message.reply(embed=embed)

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

    if len(command) == 1:
        await utils.ReplyWithException(message=message,exception_msg="Missing User and pay amount.")
        return
    if len(command) == 2:
        await utils.ReplyWithException(message=message,exception_msg="Missing User or pay amount.")
        return
    if len(command) == 3:
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
    paid_user = await singletons.client.fetch_user(user_paid_id)
    embed = discord.Embed(title=f"You have successfully Paid ${amount} to {paid_user.display_name}",color=discord.Color.green())
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
        await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))
    user_robbed = utils.FindUser(uid=user_robbed_id, sid=message.guild.id)

    if user_robbed.bank_acc.cash_on_hand < 0.5:
        await utils.ReplyWithException(message=message, exception_msg="This user is too poor!")
        return
    amount = random.uniform(user_robbed.bank_acc.cash_on_hand/4, user_robbed.bank_acc.cash_on_hand/2)
    amount = float(f"{amount:,.2f}")
    # Check if the user has enough money to rob.
    
    
    # Rob the user.
    user.bank_acc.AddCash(cash=amount)
    user_robbed.bank_acc.RemoveCash(cash=amount)
    embed = discord.Embed(description=f"You have successfully robbed ${amount} from <@{user_robbed_id}>",color=discord.Color.green())
    await message.reply(embed=embed)

async def DisplayShop(message : discord.Message) -> None:
    """Displays Shop's Items."""
    # await message.reply("Shop Command Invoked!") # Uncomment when debugging.
    embed = discord.Embed(title="Market",description="You can buy stuff here.",color=0xffff00) # Create Shop Embed.
    embed = utils.GetEmbedItemList(item_list=singletons.market, embed=embed, shop=True) # Iterates through to retrieve and use items on market.e.
    await message.reply(embed=embed)
    
    # TODO : DROP DOWN MARKETS
    # TODO : NEXT-PREVIOUS PAGE BUTTONS

async def Buy(message : discord.Message, command : list[str]) -> None:
    """Buys a specified Item with a quantity."""
    # await message.reply("Buy Command Invoked!") # Uncomment when debugging.

    command.pop(0) # Removes Prefix and action.
    command = " ".join(command)
    command = command.split("|")

    if command[0] == "": # Checks if empty.
        command.pop(0)
    
    if command.__len__() < 1: # Checks if command is with given arguments.
        await utils.ReplyWithException(message=message, exception_msg="No Item provided.. what do you want to buy?")
        return
    
    if utils.FindMarketItem(command[0]) == None: # Tries to find item.
        await utils.ReplyWithException(message=message, exception_msg="Item Not found in market. Recheck your spelling?")
        return

    buy_item = utils.FindMarketItem(command[0])
    quantity = 1

    try:
        quantity = int(command[1])
    except TypeError: # Quantity argument given wasn't an int.
        await utils.ReplyWithException(message=message, exception_msg="Invalid quantity provided. Must be a whole number.")
        return
    except IndexError: # This means that no quantity argument was even given, so just use the default (1).
        pass
        
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    item_price = buy_item.GetCost()*quantity
    
    if user.bank_acc.GetCashOnHand() < item_price : # Checks if user has enough cash on hand for item(s).
        await utils.ReplyWithException(message=message, exception_msg="Insufficient funds!", exception_desc=f"You are ${item_price-user.bank_acc.GetCashOnHand()} short.")
        return
    
    buy_item.SetQuantity(quantity) # Set quantity based on user specification.
    user.inventory.append(buy_item) # Add to User Inventory.
    user.bank_acc.RemoveCash(item_price) # Takes cost from user.
    
    embed = discord.Embed(title=f"Succesfully bought {quantity} {buy_item.GetName()}s " if quantity > 1 else f"Succesfully bought one {buy_item.GetName()}",color=discord.Color.green())
    await message.reply(embed=embed)

async def DisplayInventory(message : discord.Message) -> None:
    """Display's User's Items."""
    # await message.reply("Inventory Command Invoked!") # Uncomment when debugging.
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if user.inventory.__len__() == 0: # Empty Inventory exception.
        await utils.ReplyWithException(message=message,exception_msg="No Items in inventory.")
        return 
    
    embed = discord.Embed(title="Inventory",description="All your items.",color=discord.Color.green()) # Create Shop Embed.
    embed = utils.GetEmbedItemList(item_list=user.inventory, embed=embed, shop=False) # Iterates through to retrieve and use items on market.e.
    await message.reply(embed=embed)
