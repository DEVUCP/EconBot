# Libraries
import discord
import os
import econessentials

# Discord Essential variables
intents =  discord.Intents.all()
client = discord.Client(intents=intents)

# Constants

PREFIX = "$"
HELP_MSG ="```COMMANDS :\n$work\n$rob\n$crime\n$beg\n```"

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
        case "balance":
            await balance(message=message, command=command)
        case "work":
            await work(message=message)
        case "crime":
            await crime(message=message)
        case "beg":
            await beg(message=message)
        case "rob":
            await rob(message=message, command=command)

async def help(message : discord.Message) -> None:
    await message.reply(HELP_MSG)

async def balance(message : discord.Message, command : list[str]) -> None:
    await message.reply("Balance Command Invoked!")

    if len(command) == 1:
        user = FindUser(uid=message.author.id, sid=message.guild.id)
        await message.reply(user.bank_acc.GetBankDisplay())
        return
    user_balance_id = int(command[1].strip("<@>"))

    try: 
        await client.fetch_user(user_balance_id)
    except:
        await message.reply("Invalid user!")
        return
    
    user_balance = FindUser(uid=user_balance_id, sid=message.guild.id)
    await message.reply(user_balance.bank_acc.GetBankDisplay())

async def work(message : discord.Message) -> None:
    await message.reply("Work Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=100)
    await message.reply(user.bank_acc.GetBankDisplay())

async def crime(message : discord.Message) -> None:
    await message.reply("Crime Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=250)
    await message.reply(user.bank_acc.GetBankDisplay())

async def beg(message : discord.Message) -> None:
    await message.reply("Beg Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=50)
    await message.reply(user.bank_acc.GetBankDisplay())

async def rob(message : discord.Message, command : list[str]) -> None:
    await message.reply("Rob Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))

    try: 
        await client.fetch_user(user_robbed_id)
    except:
        await message.reply("Invalid user!")
        return
    
    user_robbed = FindUser(uid=user_robbed_id, sid=message.guild.id)

    if user_robbed.bank_acc.cash_on_hand < 50:
        await message.reply("This user is too poor!")
        return
    
    user.bank_acc.AddCash(cash=50)
    user_robbed.bank_acc.RemoveCash(cash=50)
    await message.reply(f"You have successfully robbed <@{user_robbed_id}>")

client.run(os.getenv("econtoken"))