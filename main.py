# Libraries
import discord
import os
import econessentials
import singletons
import constants
import utils
import commands
import math

# Loading

def LoadMarketPages() -> bool:
    """Loads market item list into market pages."""
    print(f"Loading market ...")
    pages = math.ceil(singletons.market.__len__() / constants.MARKET_PAGE_LEN)
    #singletons.market_pages.append(pages)
    for i in range(pages):
        for j in range(constants.MARKET_PAGE_LEN):
            try:
                singletons.market_pages[i].append(singletons.market[(constants.MARKET_PAGE_LEN*i)+j])
                print(singletons.market_pages[i])
            except IndexError:
                return True
            except Exception as e:
                print(e,singletons.market_pages[i])
                return False
        singletons.market_pages.append([]) # Adds new empty page list
    else:
        if singletons.market_pages[-1] is []:
            singletons.market_pages[-1].remove()
        return True
    

# Client Event Functions
@singletons.client.event
async def on_ready():
    # Load market in pages
    if LoadMarketPages():
        print(f"[Market Loaded Successfully !]")
        # for page in singletons.market_pages: debugging
        #    for item in page:
        #        print(item)

    print(f'--- LOGGED IN AS {singletons.client.user.name} ({singletons.client.user.id}) ---')

@singletons.client.event
async def on_message(message : discord.Message):
    if message.author.id == singletons.client.user.id: # This ignores bot's own messages.
        return
    if len(message.content) == 0: # This ignores any gif or image messages.
        return
    if message.content[0] == constants.PREFIX:
        await InvokeEcon(message=message)


async def InvokeEcon(message : discord.Message) -> None:
    """The Root Function of User-bot Interaction."""
    #await message.reply("Invoked Me!") # Uncomment when debugging.

    command = utils.GetCommand(message=message.content)
    action = command[0].lower()
    command = utils.StripEmpty(_list=command)
    match action:
        case "help":
            await commands.Help(message=message)
        case "balance":
            await commands.Balance(message=message, command=command)
        case "bal":
            await commands.Balance(message=message, command=command)
        case "withdraw":
            await commands.Withdraw(message=message, command=command)
        case "with":
            await commands.Withdraw(message=message, command=command)
        case "deposit":
            await commands.Deposit(message=message, command=command)
        case "dep":
            await commands.Deposit(message=message, command=command)
        case "pay":
            await commands.Pay(message=message, command=command)
        case "work":
            await commands.Work(message=message)
        case "crime":
            await commands.Crime(message=message)
        case "beg":
            await commands.Beg(message=message)
        case "rob":
            await commands.Rob(message=message, command=command)
        case "shop":
            await commands.DisplayShop(message=message, command=command)
        case "buy":
            await commands.Buy(message=message,command=command)
        case "inventory":
            await commands.DisplayInventory(message=message)
        case "inv":
            await commands.DisplayInventory(message=message, command=command)
        case "use":
            await commands.UseItem(message=message, command=command)
        case _: # None of the above.
            embed = discord.Embed(title="Invalid Command.. Here are a list of all the valid commands.",color=0xff0000)
            await message.reply(embed=embed)
            await commands.Help(message=message)



singletons.client.run(os.getenv("econtoken"))