
import discord
import constants
import utils
import random

slot_symbol_list = [
    ":guitar:",
    ":basketball:",
    ":fire_engine:",
    ":anchor:",
    ":trophy:",
]

async def SlotMachine(message : discord.Message, command : list[str]) -> None:
    """Plays slot machine."""
        #await message.reply("SlotMachine Command Invoked!") # Uncomment when debugging.

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

        if user.bank_acc.GetCashOnHand() >= funds and funds > constants.MIN_SLOTS_BET:
            user.bank_acc.RemoveCash(funds)

        elif funds < constants.MIN_SLOTS_BET:
            await utils.ReplyWithException(message=message, exception_msg=f"Too low of a bet.",exception_desc=f"Minimum is {constants.MIN_SLOTS_BET}.")
            return
        else:
            await utils.ReplyWithException(message=message, exception_msg="You don't have enough money to bet.",exception_desc=f"You only have {utils.ToMoney(user.bank_acc.GetCashOnHand())}.")
            return
    
    slot = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            slot[i][j] = random.choice(slot_symbol_list)
    
    win = slot[1][0] == slot[1][1] == slot[1][2]

    embed = discord.Embed()
    
    embed.set_author(
        name=message.author.display_name,  # This shows the user's display name
        icon_url=message.author.avatar.url  # This shows the user's profile picture
    )

    if win:
        user.bank_acc.AddCash(funds*2)
        embed.title = f"**You Won {utils.ToMoney(funds*2)}!**"
        embed.color = discord.Color.green()

    else:
        embed.title = f"**You Lost {utils.ToMoney(funds)}!**"
        embed.color = discord.Color.red()
    
    embed.add_field(name=f"{slot[0][0]} | {slot[0][1]} | {slot[0][2]} ",value="",inline=False)
    embed.add_field(name=f"{slot[1][0]} | {slot[1][1]} | {slot[1][2]} **<-**",value="",inline=False)
    embed.add_field(name=f"{slot[2][0]} | {slot[2][1]} | {slot[2][2]} ",value="",inline=False)
    
    await message.reply(embed=embed)

    
    

