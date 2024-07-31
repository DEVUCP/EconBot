import discord
import singletons
import econessentials
import items

def GetCommand(message : str) -> list[str]:
    """Returns a list of words from the message."""
    command = message
    command = command.strip("$") # Removes Prefix from str
    command = command.rstrip() # Removes trailing spaces
    command = command.split(" ") # Converts into list of words
    return command

def FindServer(sid : int) -> list[econessentials.User]:
    """Returns the User List from the User Dictionary."""
    # If the server is already in the dictionary, return the list of users.
    for i in singletons.user_dict.keys():
        if i == sid:
            return singletons.user_dict[i]
    # If the server is not in the dictionary, add the server to the dictionary and return an empty list.
    singletons.user_dict[sid] = []
    return singletons.user_dict[sid]

def FindUser(uid : int, sid: int) -> econessentials.User:
    """Returns the User Object from the User Dictionary."""
    # If the user is already in the list, return the user.
    server = FindServer(sid=sid)
    for i in server:
        if i.uid == uid:
            return i
    # If the user is not in the list, add the user to the list and return the user.
    singletons.user_dict[sid].append(econessentials.User(uid=uid))
    return singletons.user_dict[sid][-1]

def FindMarketItem(name : str) -> econessentials.Item:
    """Returns Item object from market list"""
    for item in singletons.market:
        if item.GetName().lower().replace(" ","") == name.lower().replace(" ",""):
            return type(item)() # Returns new instance of the same object type, not the same object.

async def GetEmbedBalance(user : econessentials.User) -> discord.Embed:
    """Returns an Embed with the User's Balance."""
    message_author = await singletons.client.fetch_user(user.uid)
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