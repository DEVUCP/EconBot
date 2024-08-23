import discord
import singletons
from utils import FindUser, ReplyWithException
from commands.display.interactables import itemlists

async def DisplayInventory(message : discord.Message, command : list[str]) -> None:
    """Display's User's Items."""
    # await message.reply("Inventory Command Invoked!") # Uncomment when debugging.

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if len(user.inventory[0]) == 0: # Empty Inventory exception.
        await ReplyWithException(message=message,exception_msg="No Items in inventory.")
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
    
    view = itemlists.InventoryView(
        original_user=message.author,
        item_list=user.inventory,
        market="Inventory",
        page = page
        ) # Creates New ItemListView    
    
    embed = view.CreateListEmbed() # Creates New ItemListView

    # Set the current page, ensuring it's within valid range (0 to last page of inventory)
    view.current_page = page if page <= len(user.inventory) - 1 and page >= 0 else len(user.inventory) - 1

    await message.reply(embed=embed, view=view)