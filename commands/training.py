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

async def Study(message : discord.Message) -> None:
    """Trains the user."""
    # await message.reply("Study Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if user.attributes["Intelligence"].IsMaxLevel():
        await ReplyWithException(message=message, exception_msg="You have already reached the maximum level for Intelligence.")
        return
    
    if user.energy.GetEnergy() <= 0:
        await ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return
    
    outcome = random.choice(constants.OUTCOMES_STUDY) # Get outcome string.

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    # Increase intelligence attribute.
    incr_amount = 1
    user.attributes["Intelligence"].IncrLevel(amount=incr_amount)
    embed = discord.Embed(title=f"+{incr_amount} Intelligence",description=outcome ,color=discord.Color.green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)

# Dexterity command
async def Paint(message : discord.Message) -> None:
    """Trains the user."""
    # await message.reply("Train Dexterity Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if user.attributes["Dexterity"].IsMaxLevel():
        await ReplyWithException(message=message, exception_msg="You have already reached the maximum level for Dexterity.")
        return
    
    if user.attributes["Creativity"].IsMaxLevel():
        await ReplyWithException(message=message, exception_msg="You have already reached the maximum level for Creativity.")
        return

    if user.energy.GetEnergy() <= 0:
        await ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    outcome = random.choice(constants.OUTCOMES_PAINT) # Get outcome string.

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    # Increase dexterity attribute.
    incr_amount = 1
    user.attributes["Dexterity"].IncrLevel(amount=incr_amount)
    user.attributes["Creativity"].IncrLevel(amount=incr_amount * 0.5)
    embed = discord.Embed(title=f"+{incr_amount} Dexterity/Creativity", description=outcome, color=discord.Color.green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)

async def Socialize(message : discord.Message) -> None:
    """Trains the user."""
    # await message.reply("Socialize Command Invoked!") # Uncomment when debugging.
    user = FindUser(uid=message.author.id, sid=message.guild.id)

    if user.attributes["Charisma"].IsMaxLevel():
        await ReplyWithException(message=message, exception_msg="You have already reached the maximum level for Charisma.")
        return
    
    if user.energy.GetEnergy() <= 0:
        await ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    outcome = random.choice(constants.OUTCOMES_SOCIALIZE) # Get outcome string.

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    # Increase charisma attribute.
    incr_amount = 1
    user.attributes["Charisma"].IncrLevel(amount=incr_amount)
    embed = discord.Embed(title=f"+{incr_amount} Charisma", description=outcome, color=discord.Color.green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)
