import discord
import constants
import utils
import random

from commands.display.interactables.blackjack import BlackJackInteractable


async def BlackJack(message : discord.Message, command : list[str]) -> None:
    """Plays a game of Blackjack."""
    #await message.reply("BlackJack Command Invoked!") # Uncomment when debugging.

    user = utils.FindUser(uid=message.author.id, sid=message.guild.id)

    if len(command) == 1:
        await utils.ReplyWithException(message=message, exception_msg="Missing funds provided.")
        return
    
    if len(command) == 2:
        command[1] = command[1].replace(",", "") # Replaces commas to be format independent.
        try:
            float(command[1])
        except:
            await utils.ReplyWithException(message=message, exception_msg="Invalid funds provided.")
            return
        
        funds = float(command[1])

        if user.bank_acc.GetCashOnHand() >= funds and funds > constants.MIN_BJ_BET:
            user.bank_acc.RemoveCash(funds)

        elif funds < constants.MIN_BJ_BET:
            await utils.ReplyWithException(message=message, exception_msg=f"Too low of a bet.",exception_desc=f"Minimum is {constants.MIN_BJ_BET}.")
            return
        else:
            await utils.ReplyWithException(message=message, exception_msg="You don't have enough money to bet.",exception_desc=f"You only have {utils.ToMoney(user.bank_acc.GetCashOnHand())}.")
            return

    user.energy.DecrEnergy(1)

    view = BlackJackInteractable(
        original_user=message.author,
        sid=message.guild.id,
        amount=funds
        )
    
    embed = view.CreateBoardEmbed(new=True)

    embed.set_author(
        name=message.author.display_name,  # This shows the user's display name
        icon_url=message.author.avatar.url  # This shows the user's profile picture
    )

    await message.reply(embed=embed, view=view)