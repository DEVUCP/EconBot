# Libraries
import discord
import os
import econessentials

# Discord Essential variables
intents =  discord.Intents.all()
client = discord.Client(intents=intents)

# Constants

PREFIX = "$"
HELP_MSG ="```COMMANDS :\n$work\n$rob\n None of these work for now.. ```"

# UTILS functions

def GetCommand(message : str) -> list[str]:
    command = message
    command = command.strip("$") # Removes Prefix from str
    command = command.rstrip() # Removes trailing spaces
    command = command.split(" ") # Converts into list of words
    return command

# Client Event Functions
@client.event
async def on_ready():
    print(f'--- LOGGED IN AS {client.user.name} ({client.user.id}) ---')

@client.event
async def on_message(message : discord.Message):
    if message.author.id == client.user.id:
        return
    
    if message.content[0] == PREFIX:
        await InvokeEcon(message=message)

#

async def InvokeEcon(message : discord.Message): # The Root Function of User-bot Interaction.
    await message.reply("Invoked Me!")

    command = GetCommand(message=message.content)
    action = command[0]

    match action:
        case "help":
            await help(message=message)

async def help(message : discord.Message):
    await message.reply(HELP_MSG)

client.run(os.getenv("econtoken"))