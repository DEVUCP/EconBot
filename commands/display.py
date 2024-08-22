import discord
import utils
import singletons
import itemlistview
import utils

from cards import CardView

async def DisplayBalance(message : discord.Message, command : list[str]) -> None:
    """Displays the balance of the user."""
   # await message.reply("DisplayBalance Command Invoked!") # Uncomment when debugging.

    # If no user is mentioned, then the balance of the user who invoked the command is displayed.
    if len(command) == 1:
        view = None
        user = utils.FindUser(uid=message.author.id, sid=message.guild.id) # Find the user who invoked the command.

        if user.bank_acc.IsCardMaxxed():
            view = CardView(original_user=message.author, message=message)
        
        embed = await utils.GetEmbedBalance(user=user)
        await message.reply(embed=embed, view=view)
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

async def DisplayClock(message : discord.Message) -> None:
    """Displays current in-game time."""
    # await message.reply("Display Clock Invoked!") # Uncomment when debugging.

    time = utils.GetClockTime(initial_time=singletons.start_time)
    
    formatted_time = time["clock"].strftime("%I:%M %p")
    week_day = time["week day"]

    color = discord.Color.dark_purple()

    if time["clock"].hour <= 5 or time["clock"].hour >= 21:
       # print("night")
        color = 0x0c072e # Dark Blurple

    elif time["clock"].hour > 5 and time["clock"].hour < 12:
       # print("morning")
        color = 0x65e3fe # light blue

    elif time["clock"].hour >= 12 and time["clock"].hour < 15:
       # print("afternoon")
        color = 0xFFD0AA # light yellow

    elif time["clock"].hour >= 17 and time["clock"].hour < 19:
       # print("early evening")
        color = 0xFD997F # light red

    elif time["clock"].hour >= 19 and time["clock"].hour < 21:
       # print("late evening")
        color = 0x526079 # light purple

    embed = discord.Embed(title=f"{week_day}, {formatted_time}",color=color)
    embed.set_footer(text=f"Day {time['days']}")

    await message.reply(embed=embed)

async def DisplayEnergy(message : discord.Message) -> None:
    """Displays user's energy bar."""
    # await message.reply("Display Energy Invoked!") # Uncomment when debugging.
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    embed = discord.Embed(title=user.energy.GetEnergyBar())
    await message.reply(embed=embed)

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
