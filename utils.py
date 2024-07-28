import discord
import global_variables
import econessentials

def GetCommand(message : str) -> list[str]:
    command = message
    command = command.strip("$") # Removes Prefix from str
    command = command.rstrip() # Removes trailing spaces
    command = command.split(" ") # Converts into list of words
    return command

def FindServer(sid : int) -> list[econessentials.User]:
    # If the server is already in the dictionary, return the list of users.
    for i in global_variables.user_dict.keys():
        if i == sid:
            return global_variables.user_dict[i]
    # If the server is not in the dictionary, add the server to the dictionary and return an empty list.
    global_variables.user_dict[sid] = []
    return global_variables.user_dict[sid]

def FindUser(uid : int, sid: int) -> econessentials.User:
    # If the user is already in the list, return the user.
    server = FindServer(sid=sid)
    for i in server:
        if i.uid == uid:
            return i
    # If the user is not in the list, add the user to the list and return the user.
    global_variables.user_dict[sid].append(econessentials.User(uid=uid))
    return global_variables.user_dict[sid][-1]

async def GetEmbedBalance(user : econessentials.User) -> discord.Embed:
    message_author = await global_variables.client.fetch_user(user.uid)
    embed = discord.Embed(title=f"{message_author.display_name}",color=discord.Color.brand_green())
    embed.set_thumbnail(url=message_author.display_avatar.url)
    embed.add_field(name="Cash:",value=f"${user.bank_acc.GetCashOnHand():,.2f}")
    embed.add_field(name="Bank:",value=f"${user.bank_acc.GetDeposit():,.2f}")
    return embed

def StripEmpty(_list : list[str]) -> list[str]:
    """Removes empty elements."""
    i = 0
    while i < len(_list):
        if len(_list[i]) == 0:
            _list.pop(i)
        else:
            i += 1
    return _list