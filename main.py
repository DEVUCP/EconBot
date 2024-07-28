# Libraries
import discord
import os
import econessentials
import global_variables
import constants
import utils
import commands


# Client Event Functions
@global_variables.client.event
async def on_ready():
    print(f'--- LOGGED IN AS {global_variables.client.user.name} ({global_variables.client.user.id}) ---')

@global_variables.client.event
async def on_message(message : discord.Message):
    if message.author.id == global_variables.client.user.id: # This ignores bot's own messages.
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
        case "withdraw":
            await commands.Withdraw(message=message, command=command)
        case "deposit":
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



global_variables.client.run(os.getenv("econtoken"))