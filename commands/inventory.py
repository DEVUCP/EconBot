import discord
from utils import FindItem, FindUser, ToMoney, ReplyWithException, FindItemInList, StripMention, IsValidMention
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

    if FindItemInList(name=command[0], item_list=user.inventory, user=user) == None: # Tries to find item.
        await ReplyWithException(message=message, exception_msg="Item Not found in Inventory. Recheck your spelling?")
        return
    
    quantity = 1

    try:
        quantity = int(command[1])

    except TypeError: # Quantity argument given wasn't an int.
        await ReplyWithException(message=message, exception_msg="Invalid quantity provided. Must be a whole number.")
        return
    
    except IndexError: # This means that no quantity argument was even given, so just use the default (1).
        pass

    sell_item = FindItemInList(name=command[0], item_list=user.inventory, user=user)

    if sell_item.GetQuantity() < quantity:
        await ReplyWithException(message=message, exception_msg=f"You don't have that many {sell_item.GetQuantity()}", exception_desc=f"You only have {sell_item.GetQuantity(), sell_item.GetName()}, not {quantity}.")

    item_for_deletion = (sell_item.GetQuantity() - quantity) == 0 # delete only if after selling the quantity will be zero
    
    sell_price = (sell_item.GetCost() - sell_item.GetCost()*0.1) * quantity # 10% loss on selling.

    user.bank_acc.AddCash(sell_price)
    sell_item.DecrQuantity(quantity)

    embed = discord.Embed(title=f"Sold {sell_item.GetName()}" if quantity == 1 else f"Sold {quantity} {sell_item.GetName()}s" ,color=discord.Color.green())
    embed.description = (f"Sold for ${sell_price:,.2f}") # 10% loss on selling.

    if item_for_deletion: # deletes item from user's inventory
        for page in user.inventory:
            item = FindItemInList(name=sell_item.GetName(), item_list=user.inventory, user=user)
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

async def Give(message : discord.Message, command : list[str]) -> None:
    """Gives a specified Item to a specified User."""
    # await message.reply("Give Command Invoked!") # Uncomment when debugging.

    command.pop(0) # Removes Prefix and action.

    
    if len(command) < 2: # Checks if command is with given arguments.
        await ReplyWithException(message=message,exception_msg="Missing Arguments.")
        return

    if await IsValidMention(command[0]): # Validates mentioned user.
        mentioned_user_id = StripMention(command[0])
    else:
        await ReplyWithException(message=message, exception_msg="Invalid user!")
        return

    sender = FindUser(uid=message.author.id, sid=message.guild.id)
    receiver = FindUser(uid=mentioned_user_id, sid=message.guild.id)

    quantity = 1
    command.pop(0) # Removes mentioned user.

    # Checks optional arguments.
    if len(command) > 2 and "|" in command:

        #<item> | <quantity>

        command = " ".join(command)
        command = command.split("|")

        if command[0] == "": # Checks if empty.
            command.pop(0)
        
        try:
            quantity = int(command[1])

            if int(quantity) < 1:
                await ReplyWithException(message=message, exception_msg="Quantity must be at least 1.")
                return

        except TypeError: # Quantity argument given wasn't an int.
            await ReplyWithException(message=message, exception_msg="Invalid quantity provided. Must be a whole number.")
            return
        
        except IndexError: # This means that no quantity argument was even given, so just use the default (1).
            pass

        
        quantity = int(command[1])
    
    item_name = command[0]

    if FindItemInList(name=item_name, item_list=sender.inventory, user=sender) == None: # Tries to find item.
        await ReplyWithException(message=message, exception_msg="Item Not found in Inventory. Recheck your spelling?")
        return
        
    sender_item = FindItemInList(name=item_name, item_list=sender.inventory, user=sender)
    receiver_item = FindItemInList(name=item_name, item_list=singletons.item_list)
    receiver_item.SetQuantity(0)
        
    if quantity > sender_item.GetQuantity(): # Checks if quantity is more than the item's quantity.
        await ReplyWithException(message=message, exception_msg="Insufficient quantity.", exception_desc=f"You cant give {quantity} {sender_item.GetName()}s, you only have {sender_item.GetQuantity()}.")
        return
    
    sender_item.DecrQuantity(decramount=quantity)
    receiver_item.IncrQuantity(incramount=quantity)
   
    if FindItemInList(name=item_name, item_list=receiver.inventory, user=receiver) == None: # Checks if user already has the item.
        receiver.AddNewItemInventory(item=receiver_item)

    else:
        receiver_item = FindItemInList(name=item_name, item_list=receiver.inventory, user=receiver)
        receiver_item.IncrQuantity(incramount=quantity)

    item_for_deletion = sender_item.GetQuantity() == 0

    reciever_disc_user = await singletons.client.fetch_user(receiver.uid)
    sender_disc_user = await singletons.client.fetch_user(sender.uid)

    embed = discord.Embed(title=f"You gave {quantity} {sender_item.GetName()}s to {reciever_disc_user.display_name}!",color=discord.Color.green())

    if item_for_deletion:
        for page in sender.inventory:
            item = FindItemInList(name=sender_item.GetName(), item_list=sender.inventory, user=sender)
            index = page.index(item)
            del page[index]
    
    await message.reply(embed=embed)

