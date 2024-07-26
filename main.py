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

# Variables

user_dict = {} # 1067541126518677664: serverid, list[econessentials.User]

# UTILS functions

def GetCommand(message : str) -> list[str]:
    command = message
    command = command.strip("$") # Removes Prefix from str
    command = command.rstrip() # Removes trailing spaces
    command = command.split(" ") # Converts into list of words
    return command

def FindServer(sid : int) -> list[econessentials.User]:
    for i in user_dict.keys():
        if i == sid:
            return user_dict[i]
    user_dict[sid] = []
    return user_dict[sid]

def FindUser(uid : int, sid: int) -> econessentials.User:
    server = FindServer(sid=sid)
    for i in server:
        if i.uid == uid:
            return i
    user_dict[sid].append(econessentials.User(uid=uid))
    return user_dict[sid][-1]

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

async def InvokeEcon(message : discord.Message) -> None: # The Root Function of User-bot Interaction.
    await message.reply("Invoked Me!")

    command = GetCommand(message=message.content)
    action = command[0]

    match action:
        case "help":
            await help(message=message)
        case "work":
            await work(message=message)

async def help(message : discord.Message) -> None:
    await message.reply(HELP_MSG)


async def work(message: discord.Message) -> None:
    await message.reply("Work Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=100)
    await message.reply(user.bank_acc.GetBankDisplay())

client.run(os.getenv("econtoken"))