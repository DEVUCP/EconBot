import discord
import random
import utils
import constants
import singletons

async def Crime(message : discord.Message) -> None:
    """Commits a crime for money."""
    # await message.reply("Crime Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    # CHECK USER'S ENERGY
    if user.energy.GetEnergy() <= 0:
        await utils.ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    crime_check = random.randint(0, 100)
    outcome_pool = constants.OUTCOMES_CRIME
    crime_success = True

    if crime_check <= constants.CRIME_FAIL_PERCENTAGE:
        crime_success = False
        outcome_pool = constants.OUTCOMES_FAIL_CRIME

        # Reduce user's employability.
        user.attributes["Employability"].DecrLevel(amount=1)
    
    outcome = random.choice(outcome_pool) # Get outcome string.
    value_1, value_2 = constants.CRIME_PAY # Get outcome money range.

    
    # Randomize cash.
    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    final_outcome = outcome.replace("#", str(abs(cash)))

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green() if crime_success else discord.Color.brand_red())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)