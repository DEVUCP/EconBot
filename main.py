# Libraries
import discord
import os
import commands.bank
import commands.display
import commands.earnings
import commands.inventory
import commands.misc
import singletons
import constants
import utils
import saveload
import commands

# Client Event Functions
@singletons.client.event
async def on_ready():
    # Loads first
    if os.path.exists("userdata.pkl") and saveload.LoadAll():
        print(f'--- LOGGED IN AS {singletons.client.user.name} ({singletons.client.user.id}) ---')

@singletons.client.event
async def on_message(message : discord.Message):
    if not saveload.loaded:
        return
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
            await commands.misc.Help(message=message)
        case "balance":
            await commands.bank.Balance(message=message, command=command)
        case "bal":
            await commands.bank.Balance(message=message, command=command)
        case "withdraw":
            await commands.bank.Withdraw(message=message, command=command)
        case "with":
            await commands.bank.Withdraw(message=message, command=command)
        case "deposit":
            await commands.bank.Deposit(message=message, command=command)
        case "dep":
            await commands.bank.Deposit(message=message, command=command)
        case "pay":
            await commands.bank.Pay(message=message, command=command)
        case "work":
            await commands.earnings.Work(message=message)
        case "crime":
            await commands.earnings.Crime(message=message)
        case "beg":
            await commands.earnings.Beg(message=message)
        case "rob":
            await commands.earnings.Rob(message=message, command=command)
        case "shop":
            await commands.display.DisplayMarket(message=message, command=command)
        case "market":
            await commands.display.DisplayMarket(message=message, command=command)
        case "buy":
            await commands.inventory.Buy(message=message, command=command)
        case "sell":
            await commands.inventory.Sell(message=message, command=command)
        case "inventory":
            await commands.display.DisplayInventory(message=message)
        case "inv":
            await commands.display.DisplayInventory(message=message, command=command)
        case "use":
            await commands.UseItem(message=message, command=command)
        case _: # None of the above.
            embed = discord.Embed(title="Invalid Command.. Here are a list of all the valid commands.",color=0xff0000)
            await message.reply(embed=embed)
            await commands.Help(message=message)


singletons.client.run(os.getenv("econtoken"))