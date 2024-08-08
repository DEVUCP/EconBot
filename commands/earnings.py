import discord
import random
import utils
import constants
import singletons

async def Work(message : discord.Message) -> None:
    """Works for money."""
    # await message.reply("Work Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    outcome = random.choice(list(constants.OUTCOMES_WORK.keys())) # Get outcome string.
    value_1, value_2 = constants.OUTCOMES_WORK[outcome] # Get outcome money range.

    # Randomize cash.
    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    final_outcome = outcome.replace("#", str(cash))

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green())
    await message.reply(embed=embed)

async def Crime(message : discord.Message) -> None:
    """Commits a crime for money."""
    # await message.reply("Crime Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    outcome = random.choice(list(constants.OUTCOMES_CRIME.keys())) # Get outcome string.
    value_1, value_2 = constants.OUTCOMES_CRIME[outcome] # Get outcome money range.

    # Randomize cash.
    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    final_outcome = outcome.replace("#", str(cash))

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green())
    await message.reply(embed=embed)

async def Beg(message : discord.Message) -> None:
    """Begs for money."""
    # await message.reply("Beg Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    
    outcome = random.choice(list(constants.OUTCOMES_BEG.keys())) # Get outcome string.
    value_1, value_2 = constants.OUTCOMES_BEG[outcome] # Get outcome money range.

    # Randomize cash.
    cash = random.uniform(value_1, value_2)
    cash = float(f"{cash:,.2f}")

    # Add cash to user.
    user.bank_acc.AddCash(cash=cash)

    final_outcome = outcome.replace("#", str(cash))

    embed = discord.Embed(description=final_outcome,color=discord.Color.brand_green())
    await message.reply(embed=embed)

async def Rob(message : discord.Message, command : list[str]) -> None:
    """Rob another user for money."""
    # await message.reply("Rob Command Invoked!") # Uncomment when debugging.
    
    # Check if the user is valid.
    try: 
        user_robbed_id = int(command[1].strip("<@>"))
        await singletons.client.fetch_user(user_robbed_id)
    except:
        await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))
    user_robbed = utils.FindUser(uid=user_robbed_id, sid=message.guild.id)

    # Check if the user has enough money to rob.
    if user_robbed.bank_acc.cash_on_hand < 0.5:
        await utils.ReplyWithException(message=message, exception_msg="This user is too poor!")
        return
    
    amount = random.uniform(user_robbed.bank_acc.cash_on_hand/4, user_robbed.bank_acc.cash_on_hand/2)
    amount = float(f"{amount:,.2f}")
    
    # Rob the user.
    user.bank_acc.AddCash(cash=amount)
    user_robbed.bank_acc.RemoveCash(cash=amount)

    embed = discord.Embed(description=f"You have successfully robbed ${amount} from <@{user_robbed_id}>",color=discord.Color.green())
    await message.reply(embed=embed)