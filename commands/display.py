import discord
import utils
import singletons
import itemlistview

async def DisplayMarket(message : discord.Message, command : list[str]) -> None:
    """Displays Market's Items."""
    # await message.reply("Market Command Invoked!") # Uncomment when debugging.

    page = 0
    command.pop(0) # removes prefix.

    if not command:
        try: # If given valid page number will use it.
            if len(singletons.market_pages) - 1 >= int(command[0]):
                page = int(command[0])
            else:
                page = -1

        except TypeError:
            pass
        
        except IndexError:
            pass

    initial_embed = itemlistview.CreateListEmbed(page=page, item_list=singletons.market_pages, market="Market") # Makes Initial Embed from page 0.
    view = itemlistview.MarketView(original_user=message.author, item_list=singletons.market_pages, market="Market") # Creates New ItemListView

    # Set the current page, ensuring it's within valid range (0 to last page of market)
    view.current_page = page if page <= len(singletons.market_pages) - 1 and page >= 0 else len(singletons.market_pages) - 1

    await message.reply(embed=initial_embed, view=view)

async def DisplayBlackMarket(message : discord.Message, command : list[str]) -> None:
    """Displays BlackMarket's Items."""
    # await message.reply("BlackMarket Command Invoked!") # Uncomment when debugging.

    page = 0
    command.pop(0) # removes prefix.

    if not command:
        try: # If given valid page number will use it.
            if len(singletons.black_market_pages) - 1 >= int(command[0]):
                page = int(command[0])
            else:
                page = -1

        except TypeError:
            pass
        
        except IndexError:
            pass

    initial_embed = itemlistview.CreateListEmbed(page=page, item_list=singletons.black_market_pages, market="Black Market") # Makes Initial Embed from page 0.
    view = itemlistview.MarketView(message.author,item_list=singletons.black_market_pages, market="Black Market") # Creates New ItemListView

    # Set the current page, ensuring it's within valid range (0 to last page of market)
    view.current_page = page if page <= len(singletons.black_market_pages) - 1 and page >= 0 else len(singletons.market_pages) - 1

    await message.reply(embed=initial_embed, view=view)

async def DisplayInventory(message : discord.Message, command : list[str]) -> None:
    """Display's User's Items."""
    # await message.reply("Inventory Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if len(user.inventory[0]) == 0: # Empty Inventory exception.
        await utils.ReplyWithException(message=message,exception_msg="No Items in inventory.")
        return 
    
    page = 0
    command.pop(0) # removes prefix.

    if not command:
        try: # If given valid page number will use it.
            if len(user.inventory) - 1 >= int(command[0]):
                page = int(command[0])

            else:
                page = -1

        except TypeError:
            pass

        except IndexError:
            pass
    
    initial_embed = itemlistview.CreateListEmbed(page=page, item_list=user.inventory) # Makes Initial Embed from page 0.
    view = itemlistview.InventoryView(message.author,item_list=user.inventory) # Creates New ItemListView

    # Set the current page, ensuring it's within valid range (0 to last page of inventory)
    view.current_page = page if page <= len(user.inventory) - 1 and page >= 0 else len(user.inventory) - 1

    await message.reply(embed=initial_embed, view=view)
