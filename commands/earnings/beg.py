import discord
import random
import utils
import constants
import singletons

async def Beg(message : discord.Message) -> None:
    """Begs for money."""
    # await message.reply("Beg Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    if user.energy.GetEnergy() <= 0:
        await utils.ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    outcome = random.choice(list(constants.OUTCOMES_BEG.keys())) # Get outcome string.
    value_1, value_2 = constants.OUTCOMES_BEG[outcome] # Get outcome money range.

    # Randomize cash.
    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    # Reduce user's employability.
    user.attributes["Employability"].DecrLevel(amount=0.5)

    final_outcome = outcome.replace("#", str(cash))

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)