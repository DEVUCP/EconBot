import discord
from utils import FindItem, FindUser, ToMoney, ReplyWithException, FindItemInList
import singletons

async def Buy(message : discord.Message, command : list[str]) -> None:
    """Buys a specified Item with a quantity."""
    # await message.reply("Buy Command Invoked!") # Uncomment when debugging.

    command.pop(0) # Removes Prefix and action.
    command = " ".join(command)
    command = command.split("|")

    if command[0] == "": # Checks if empty.
        command.pop(0)
    
    if len(command) < 1: # Checks if command is with given arguments.
        await ReplyWithException(message=message, exception_msg="No Item provided.. what do you want to buy?")
        return
    
    if FindItem(name=command[0]) == None: # Tries to find item.
        await ReplyWithException(message=message, exception_msg="Item Not found in market. Recheck your spelling?")
        return

    buy_item = FindItem(name=command[0])
    quantity = 1

    try:
        quantity = int(command[1])

    except TypeError: # Quantity argument given wasn't an int.
        await ReplyWithException(message=message, exception_msg="Invalid quantity provided. Must be a whole number.")
        return
    
    except IndexError: # This means that no quantity argument was even given, so just use the default (1).
        pass
        
    user = FindUser(uid=message.author.id, sid=message.guild.id)
    item_price = buy_item.GetCost()*quantity
    
    if user.bank_acc.GetCashOnHand() < item_price : # Checks if user has enough cash on hand for item(s).
        await ReplyWithException(message=message, exception_msg="Insufficient funds!", exception_desc=f"You are {ToMoney(item_price-user.bank_acc.GetCashOnHand())} short.")
        return
    
    if FindItemInList(name=command[0], item_list=user.inventory, user=user): # if Object already exists in inventory will just increment quantity
        item = FindItemInList(name=command[0], item_list=user.inventory, user=user)
        item.IncrQuantity(quantity)

    else: # Else add new item.
        buy_item.SetQuantity(quantity) # Set quantity based on user specification.
        user.AddNewItemInventory(buy_item)

    user.bank_acc.RemoveCash(item_price) # Takes cost from user.
    
    embed = discord.Embed(
        title=f"Succesfully bought {quantity} {buy_item.GetName()}s " if quantity > 1 
        else f"Succesfully bought one {buy_item.GetName()}",
        description=f"{ToMoney(user.bank_acc.GetCashOnHand())} leftover cash.",
        color=discord.Color.green()
        )
    await message.reply(embed=embed)

async def Sell(message : discord.Message, command : list[str]) -> None:
    """Sells a specified Item with a quantity."""
    # await message.reply("Sell Command Invoked!") # Uncomment when debugging.

    command.pop(0) # Removes Prefix and action.
    command = " ".join(command)
    command = command.split("|")

    if command[0] == "": # Checks if empty.
        command.pop(0)
    
    if len(command) < 1: # Checks if command is with given arguments.
        await ReplyWithException(message=message, exception_msg="No Item provided.. what do you want to sell?")
        return
    
    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if FindItem(name=command[0], item_list=user.inventory, user=user) == None: # Tries to find item.
        await ReplyWithException(message=message, exception_msg="Item Not found in Inventory. Recheck your spelling?")
        return
    
    sell_item = FindItem(name=command[0], item_list=user.inventory, user=user)
    item_for_deletion = sell_item.GetQuantity() == 1
    
    user.bank_acc.AddCash(sell_item.GetCost() - sell_item.GetCost()*0.1) # 10% loss on selling.

    embed = discord.Embed(title="SOLD!!",color=discord.Color.green())
    embed.description = (f"Sold for {sell_item.GetCost() - sell_item.GetCost()*0.1}") # 10% loss on selling.

    if item_for_deletion:
        for page in user.inventory:
            item = FindItem(name=sell_item.GetName(), item_list=user.inventory, user=user)
            index = page.index(item)
            del page[index]
    
    await message.reply(embed=embed)

async def UseItem(message : discord.Message, command : list[str]) -> None:
    """Uses a specified Item."""
    # await message.reply("Use Command Invoked!") # Uncomment when debugging.

    command.pop(0) # Removes Prefix and action.
    command = " ".join(command)
    command = command.split("|")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if command[0] == "": # Checks if empty.
        command.pop(0)
    
    if len(command) < 1: # Checks if command is with given arguments.
        await ReplyWithException(message=message, exception_msg="No Item provided.. what do you want to use?")
        return
    
    if FindItemInList(name=command[0], item_list=user.inventory, user=user) == None: # Tries to find item.
        await ReplyWithException(message=message, exception_msg="Item Not found in Inventory. Recheck your spelling?")
        return

    use_item = FindItemInList(name=command[0], item_list=user.inventory, user=user)
    item_for_deletion = use_item.GetQuantity() == 1
    
    embed = discord.Embed(title=use_item.Use(user=user),color=discord.Color.green())
    if item_for_deletion:
        for page in user.inventory:
            item = FindItemInList(name=use_item.GetName(), item_list=user.inventory, user=user)
            index = page.index(item)
            del page[index]
    
    await message.reply(embed=embed)
