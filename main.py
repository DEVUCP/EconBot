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
    # If the server is already in the dictionary, return the list of users.
    for i in user_dict.keys():
        if i == sid:
            return user_dict[i]
    # If the server is not in the dictionary, add the server to the dictionary and return an empty list.
    user_dict[sid] = []
    return user_dict[sid]

def FindUser(uid : int, sid: int) -> econessentials.User:
    # If the user is already in the list, return the user.
    server = FindServer(sid=sid)
    for i in server:
        if i.uid == uid:
            return i
    # If the user is not in the list, add the user to the list and return the user.
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
            await Balance(message=message, command=command)
        case "work":
            await Work(message=message)
        case "crime":
            await Crime(message=message)
        case "beg":
            await Beg(message=message)
        case "rob":
            await Rob(message=message, command=command)

async def Help(message : discord.Message) -> None:
    await message.reply(HELP_MSG)

async def Balance(message : discord.Message, command : list[str]) -> None:
    await message.reply("Balance Command Invoked!")

    # If no user is mentioned, then the balance of the user who invoked the command is displayed.
    if len(command) == 1:
        user = FindUser(uid=message.author.id, sid=message.guild.id) # Find the user who invoked the command.
        await message.reply(f"<@{user.uid}>'s Account:\n{user.bank_acc.GetBankDisplay()}")
        return
    # If a user is mentioned, then the balance of the mentioned user is displayed.
    user_balance_id = int(command[1].strip("<@>"))

    # Check if the user is valid.
    try: 
        await client.fetch_user(user_balance_id)
    except:
        await message.reply("Invalid user!")
        return
    
    # Display the balance of the mentioned user.
    user_balance = FindUser(uid=user_balance_id, sid=message.guild.id)
    await message.reply(user_balance.bank_acc.GetBankDisplay())

async def Work(message : discord.Message) -> None:
    await message.reply("Work Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=100)
    await message.reply(user.bank_acc.GetBankDisplay())

async def Crime(message : discord.Message) -> None:
    await message.reply("Crime Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=250)
    await message.reply(user.bank_acc.GetBankDisplay())

async def Beg(message : discord.Message) -> None:
    await message.reply("Beg Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=50)
    await message.reply(user.bank_acc.GetBankDisplay())

async def Rob(message : discord.Message, command : list[str]) -> None:
    amount = 50
    await message.reply("Rob Command Invoked!")

    user = FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))

    # Check if the user is valid.
    try: 
        await client.fetch_user(user_robbed_id)
    except:
        await message.reply("Invalid user!")
        return
    
    user_robbed = FindUser(uid=user_robbed_id, sid=message.guild.id)

    # Check if the user has enough money to rob.
    if user_robbed.bank_acc.cash_on_hand < amount:
        await message.reply("This user is too poor!")
        return
    
    # Rob the user.
    user.bank_acc.AddCash(cash=amount)
    user_robbed.bank_acc.RemoveCash(cash=amount)
    await message.reply(f"You have successfully robbed {amount} from <@{user_robbed_id}>")

client.run(os.getenv("econtoken"))