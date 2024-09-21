import discord
import random
import utils
import constants
import singletons

async def Rob(message : discord.Message, command : list[str]) -> None:
    """Rob another user for money."""
    # await message.reply("Rob Command Invoked!") # Uncomment when debugging.
    
    # Check if the user is valid.

    if len(command) < 2:
        await utils.ReplyWithException(message=message, exception_msg="Missing user!")
        return
    
    if await utils.IsValidMention(command[1]):
        mentioned_user_id = utils.StripMention(command[1])
    else:
        await utils.ReplyWithException(message=message, exception_msg="Invalid user!")
        return
    
    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
    user_robbed_id = int(command[1].strip("<@>"))
    user_robbed = utils.FindUser(uid=user_robbed_id, sid=message.guild.id)

    if user.energy.GetEnergy() <= 0:
        await utils.ReplyWithException(message=message, exception_msg="Energy insufficient.", exception_desc="Try waiting a bit to replenish your energy.")
        return

    # Check if the user has enough money to rob.
    if user_robbed.bank_acc.cash_on_hand < 0.5:
        await utils.ReplyWithException(message=message, exception_msg="This user is too poor!")
        return
    
    amount = random.uniform(user_robbed.bank_acc.cash_on_hand/4, user_robbed.bank_acc.cash_on_hand/2)
    amount = float(f"{amount:,.2f}")
    
    # Rob the user.
    user.bank_acc.AddCash(cash=amount)
    user_robbed.bank_acc.RemoveCash(cash=amount)

    # Take energy from user.
    user.energy.DecrEnergy(amount=1)

    embed = discord.Embed(description=f"You have successfully robbed ${amount} from <@{user_robbed_id}>",color=discord.Color.green())
    embed.set_footer(text=user.energy.GetEnergyBar())
    await message.reply(embed=embed)