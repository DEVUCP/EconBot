import discord
import singletons
from utils import GetClockTime, FindUser

async def DisplayClock(message : discord.Message) -> None:
    """Displays current in-game time."""
    # await message.reply("Display Clock Invoked!") # Uncomment when debugging.

    time = GetClockTime(initial_time=singletons.start_time)
    
    formatted_time = time["clock"].strftime("%I:%M %p")
    week_day = time["week day"]

    color = discord.Color.dark_purple()

    if time["clock"].hour <= 5 or time["clock"].hour >= 21:
       # print("night")
        color = 0x0c072e # Dark Blurple

    elif time["clock"].hour > 5 and time["clock"].hour < 12:
       # print("morning")
        color = 0x65e3fe # light blue

    elif time["clock"].hour >= 12 and time["clock"].hour < 15:
       # print("afternoon")
        color = 0xFFD0AA # light yellow

    elif time["clock"].hour >= 17 and time["clock"].hour < 19:
       # print("early evening")
        color = 0xFD997F # light red

    elif time["clock"].hour >= 19 and time["clock"].hour < 21:
       # print("late evening")
        color = 0x526079 # light purple

    embed = discord.Embed(title=f"{week_day}, {formatted_time}",color=color)
    embed.set_footer(text=f"Day {time['days']}")

    await message.reply(embed=embed)

