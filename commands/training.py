import random
import constants
import discord
from utils import FindUser, ReplyWithException

async def Workout(message : discord.Message) -> None:
    """Trains the user."""
    # await message.reply("Workout Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if user.attributes["Strength"].IsMaxLevel():
        await ReplyWithException(message=message, exception_msg="You have already reached the maximum level for Strength.")
        return

    if user.energy.GetEnergy() <= 0:
        await ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    outcome = random.choice(constants.OUTCOMES_WORKOUT) # Get outcome string.

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    # Increase strength attribute.
    incr_amount = 1
    user.attributes["Strength"].IncrLevel(amount=incr_amount)

    embed = discord.Embed(title=f"+{incr_amount} Strength",description=outcome ,color=discord.Color.green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)