import discord
import random
import utils
import constants
import singletons

async def Work(message : discord.Message) -> None:
    """Works for money."""
    # await message.reply("Work Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    # CHECK USER'S ENERGY
    if user.energy.GetEnergy() <= 0:
        await utils.ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    if user.occupation.GetName() == "Unemployed":
        outcome = random.choice(list(constants.OUTCOMES_WORK.keys())) # Get outcome string.
        value_1, value_2 = constants.OUTCOMES_WORK[outcome] # Get outcome money range.

    # Randomize cash.
        cash = random.uniform(value_1, value_2)
        cash = float(f"{cash:,.2f}")

        final_outcome = outcome.replace("#", str(cash))
    else:
        cash = user.GetIncome()
        user.attributes["Employability"].IncrLevel(amount=0.5)
        final_outcome = f"You worked as a {user.occupation.GetName()} and earned ${cash:,.2f}."

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)
