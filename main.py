# Libraries
import discord
import os
import econessentials

# Discord Essential variables
intents =  discord.Intents.all()
client = discord.Client(intents=intents)

# Constants

PREFIX = "$"
HELP_MSG ="```COMMANDS :\n$balance\n$withdraw\n$deposit\n$work\n$rob\n$crime\n$beg\n```"

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

async def GetEmbedBalance(user : econessentials.User) -> discord.Embed:
    message_author = await client.fetch_user(user.uid)
    embed = discord.Embed(title=f"{message_author.display_name}",color=discord.Color.brand_green())
    embed.set_thumbnail(url=message_author.display_avatar.url)
    embed.add_field(name="Cash:",value=f"${user.bank_acc.GetCashOnHand():,.2f}")
    embed.add_field(name="Bank:",value=f"${user.bank_acc.GetDeposit():,.2f}")
    return embed

# Client Event Functions
@client.event
async def on_ready():
    print(f'--- LOGGED IN AS {client.user.name} ({client.user.id}) ---')

@client.event
async def on_message(message : discord.Message):
    if message.author.id == client.user.id: # This ignores bot's own messages.
        return
    if len(message.content) == 0: # This ignores any gif or image messages.
        return
    if message.content[0] == PREFIX:
        await InvokeEcon(message=message)

#

async def InvokeEcon(message : discord.Message) -> None: # The Root Function of User-bot Interaction.
    #await message.reply("Invoked Me!") # Uncomment when debugging.

    command = GetCommand(message=message.content)
    action = command[0]

    match action:
        case "help":
            await help(message=message)
        case "balance":
            await Balance(message=message, command=command)
        case "withdraw":
            await Withdraw(message=message, command=command)
        case "deposit":
            await Deposit(message=message, command=command)
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
   # await message.reply("Balance Command Invoked!") # Uncomment when debugging.

    # If no user is mentioned, then the balance of the user who invoked the command is displayed.
    if len(command) == 1:
        user = FindUser(uid=message.author.id, sid=message.guild.id) # Find the user who invoked the command.
        embed = await GetEmbedBalance(user=user)
        await message.reply(embed=embed)
        return
    # If a user is mentioned, then the balance of the mentioned user is displayed.
    mentioned_user_id = int(command[1].strip("<@>"))
    # Check if the user is valid.
    try: 
        await client.fetch_user(mentioned_user_id)
    except:
        await message.reply("Invalid user!")
        return
    # Display the balance of the mentioned user.
    mentioned_user = FindUser(uid=mentioned_user_id, sid=message.guild.id)
    embed = await GetEmbedBalance(user=mentioned_user)
    await message.reply(embed=embed)

async def Withdraw(message : discord.Message, command : list[str]) -> None:
    # await message.reply("Withdraw Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)
    if len(command) == 1:
        embed = discord.Embed(title=f"Succesfully withdrawn {user.bank_acc.GetDeposit():,.2f}")
        user.bank_acc.WithdrawAmount(user.bank_acc.GetDeposit())
        await message.reply(embed=embed)
        return
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            embed = discord.Embed(title="Invalid funds provided.") 
            await message.reply(embed=embed)
            return
        funds = float(command[1])
        if user.bank_acc.GetDeposit() >= funds and funds > 0.00:
            user.bank_acc.WithdrawAmount(funds)
            embed = discord.Embed(title=f"Succesfully withdrawn {funds:,.2f}")
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient funds.")  
            await message.reply(embed=embed)

async def Deposit(message : discord.Message, command : list[str]) -> None:
    # await message.reply("Deposit Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)
    if len(command) == 1:
        embed = discord.Embed(title=f"Succesfully deposited {user.bank_acc.GetCashOnHand():,.2f}")
        user.bank_acc.DepositAmount(user.bank_acc.GetCashOnHand())
        await message.reply(embed=embed)
        return
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            embed = discord.Embed(title="Invalid funds provided.") 
            await message.reply(embed=embed)
            return
        funds = float(command[1])
        if user.bank_acc.GetCashOnHand() >= funds and funds > 0.00:
            user.bank_acc.DepositAmount(funds)
            embed = discord.Embed(title=f"Succesfully Deposited {funds:,.2f}")
            await message.reply(embed=embed)
        else:
            embed = discord.Embed(title="Insufficient funds.")  
            await message.reply(embed=embed)
    

async def Work(message : discord.Message) -> None:
    # await message.reply("Work Command Invoked!") # Uncomment when debugging.


    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=1300)
    embed = await GetEmbedBalance(user=user)
    await message.reply(embed=embed)

async def Crime(message : discord.Message) -> None:
    # await message.reply("Crime Command Invoked!") # Uncomment when debugging.

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=250)
    embed = await GetEmbedBalance(user=user)
    await message.reply(embed=embed)


async def Beg(message : discord.Message) -> None:
    # await message.reply("Beg Command Invoked!") # Uncomment when debugging.

    user = FindUser(uid=message.author.id, sid=message.guild.id)

    user.bank_acc.AddCash(cash=50)
    embed = await GetEmbedBalance(user=user)
    await message.reply(embed=embed)

async def Rob(message : discord.Message, command : list[str]) -> None:
    amount = 50
    # await message.reply("Rob Command Invoked!") # Uncomment when debugging.

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