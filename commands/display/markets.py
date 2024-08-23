import discord
import singletons
from commands.display.interactables import itemlists


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

    view = itemlists.MarketView(
        original_user=message.author,
        item_list=singletons.market_pages,
        market="Market",
        page = page
        ) # Creates New ItemListView    
    
    embed = view.CreateListEmbed() # Creates New ItemListView
    
    # Set the current page, ensuring it's within valid range (0 to last page of market)
    view.current_page = page if page <= len(singletons.market_pages) - 1 and page >= 0 else len(singletons.market_pages) - 1

    await message.reply(embed=embed, view=view)

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

    view = itemlists.MarketView(
        original_user=message.author,
        item_list=singletons.black_market_pages,
        market="Black Market",
        page = page
        ) # Creates New ItemListView

    embed = view.CreateListEmbed() # Creates New ItemListView

    # Set the current page, ensuring it's within valid range (0 to last page of market)
    view.current_page = page if page <= len(singletons.black_market_pages) - 1 and page >= 0 else len(singletons.market_pages) - 1

    await message.reply(embed=embed, view=view)