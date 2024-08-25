import discord
import singletons

from econ import user
import constants
import datetime

def ToMoney(amount: float) -> str:
    """Returns the amount in money format."""
    return f"${amount:.2f}"

def GetCommand(message : str) -> list[str]:
    """Returns a list of words from the message."""
    command = message
    command = command.strip("$") # Removes Prefix from str
    command = command.rstrip() # Removes trailing spaces
    command = command.split(" ") # Converts into list of words

    return command

def FindServer(sid : int) -> list[user.User]:
    """Returns the User List from the User Dictionary."""
    # If the server is already in the dictionary, return the list of users.
    for i in singletons.user_dict.keys():
        if i == sid:
            return singletons.user_dict[i]
        
    # If the server is not in the dictionary, add the server to the dictionary and return an empty list.
    singletons.user_dict[sid] = []

    return singletons.user_dict[sid]

def FindUser(uid : int, sid: int) -> user.User:
    """Returns the User Object from the User Dictionary."""
    # If the user is already in the list, return the user.
    server = FindServer(sid=sid)

    for i in server:
        if i.uid == uid:
            return i
        
    # If the user is not in the list, add the user to the list and return the user.
    singletons.user_dict[sid].append(user.User(uid=uid))

    return singletons.user_dict[sid][-1]

async def ReplyWithException(message: discord.Message, exception_msg: str = "Exception!", exception_desc: str = "") -> None:
    """Replies to message that caused an exception with exception detail."""
    embed = discord.Embed(
        title=exception_msg,
        color=constants.EXCEPTION_COLOR,
        description=exception_desc
    )
    await message.reply(embed=embed)

def FindItemInList(name : str, item_list, user = None):# -> econessentials.Item:
    """Returns Item object from item list."""
    if user != None:
        for page in item_list:
            for item in page:
                if item.GetName().lower().replace(" ","") == name.lower().replace(" ",""):
                        return item
        return None
    else:
        for item in item_list:
            if item.GetName().lower().replace(" ","") == name.lower().replace(" ",""):
                return type(item)() # Returns new instance of the same object type, not the same object.
        return None

def FindItem(name : str, user : user.User = None):
    for market in [singletons.market, singletons.black_market]:
        item = FindItemInList(name=name, item_list=market, user=user)
        if item != None:
            return item
    return None

def StripEmpty(_list : list[str]) -> list[str]:
    """Removes empty elements."""
    i = 0
    while i < len(_list):
        if len(_list[i]) == 0:
            _list.pop(i)
        else:
            i += 1
    return _list


def GetTimeDelta(initial_time : datetime.datetime):
    """Returns the time delta between the current time and the given time in game time."""
    time_delta = datetime.datetime.now() - initial_time

    hours, remainder = divmod(time_delta.seconds, 3600) 
    minutes, seconds = divmod(remainder, 60)
    

    return {
        "days": hours,
        "hours": minutes,
        "minutes": seconds,
    }


def GetClockTime(initial_time : datetime.datetime):
    """Returns the time delta between the current time and the given time in game clock time and the day of the week in a dictionary."""
    time_delta = datetime.datetime.now() - initial_time

    hours, remainder = divmod(time_delta.seconds, 3600) 
    minutes, seconds = divmod(remainder, 60)

    # Shifts every one to the left to convert to in game time.
    ingame_days = hours
    ingame_hours = minutes % 24
    ingame_minutes = seconds % 60

    clocktime = datetime.datetime.strptime(f"{ingame_hours}:{ingame_minutes}", "%H:%M")

    week_day = GetWeekDay(days=ingame_days)

    return {
    "clock": clocktime,
    "week day":week_day,
    "days":ingame_days,
    }

def GetWeekDay(days : int) -> str:
    """Returns the day of the week from the given number of days elapsed."""
    match days % 7:
        case 0:
            return "Mon"
        case 1:
            return "Tue"
        case 2:
            return "Wed"
        case 3:
            return "Thu"
        case 4:
            return "Fri"
        case 5:
            return "Sat"
        case 6:
            return "Sun"
        case 0:
            return "Mon"
        case _:
            return "Error"