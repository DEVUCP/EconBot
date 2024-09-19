# Libraries
import discord
import os

import singletons
import constants
import utils
from saveload import saveload
from econ.jobs import listings
import commands
from commands import bank, earnings, inventory, display, training, apply
from commands.display import balance, markets, inventory, clock, energy, help, profile, jobs

# Client Event Functions
@singletons.client.event
async def on_ready():
    # Loads first
    listings.GenerateListings()
    if os.path.exists(saveload.save_path) and saveload.LoadAll():
        print(f'--- LOGGED IN AS {singletons.client.user.name} ({singletons.client.user.id}) ---')

@singletons.client.event
async def on_message(message : discord.Message):
    if not saveload.loaded:
        return
    if message.author.id == singletons.client.user.id: # This ignores bot's own messages.
        return
    if len(message.content) == 0: # This ignores any gif or image messages.
        return
    if message.content[0] == constants.PREFIX:
        await InvokeEcon(message=message)
    if message.content == "please??":
        user = utils.FindUser(uid=message.author.id, sid=message.guild.id)
        user.bank_acc.AddCash(5000.00)


async def InvokeEcon(message : discord.Message) -> None:
    """The Root Function of User-bot Interaction."""
    #await message.reply("Invoked Me!") # Uncomment when debugging.

    command = utils.GetCommand(message=message.content)
    action = command[0].lower()
    command = utils.StripEmpty(_list=command)
    match action:
        case "help":
            await commands.display.help.Help(message=message, command=command)
        case "balance":
            await commands.display.balance.DisplayBalance(message=message, command=command)
        case "bal":
            await commands.display.balance.DisplayBalance(message=message, command=command)
        case "profile":
            await commands.display.profile.DisplayProfile(message=message, command=command)
        case "withdraw":
            await commands.bank.Withdraw(message=message, command=command)
        case "with":
            await commands.bank.Withdraw(message=message, command=command)
        case "deposit":
            await commands.bank.Deposit(message=message, command=command)
        case "dep":
            await commands.bank.Deposit(message=message, command=command)
        case "pay":
            await commands.bank.Pay(message=message, command=command)
        case "work":
            await commands.earnings.Work(message=message)
        case "crime":
            await commands.earnings.Crime(message=message)
        case "beg":
            await commands.earnings.Beg(message=message)
        case "rob":
            await commands.earnings.Rob(message=message, command=command)
        case "workout":
            await commands.training.Workout(message=message)
        case "excercise":
            await commands.training.Workout(message=message)
        case "study":
            await commands.training.Study(message=message)
        case "paint":
            await commands.training.Paint(message=message)
        case "socialize":
            await commands.training.Socialize(message=message)
        case "shop":
            await commands.display.markets.DisplayMarket(message=message, command=command)
        case "market":
            await commands.display.markets.DisplayMarket(message=message, command=command)
        case "jobs":
            await commands.display.jobs.DisplayJobs(message=message)
        case "apply":
            await commands.apply.Apply(message=message, command=command)
        case "info":
            await commands.display.jobs.DisplayJobInfo(message=message, command=command)
        case "buy":
            await commands.inventory.Buy(message=message, command=command)
        case "sell":
            await commands.inventory.Sell(message=message, command=command)
        case "inventory":
            await commands.display.inventory.DisplayInventory(message=message)
        case "inv":
            await commands.display.inventory.DisplayInventory(message=message, command=command)
        case "use":
            await commands.inventory.UseItem(message=message, command=command)
        case "clock":
            await commands.display.clock.DisplayClock(message=message)
        case "energy":
            await commands.display.energy.DisplayEnergy(message=message)
        case "bj":
            await blackjack(message=message)
        case _: # None of the above.
            embed = discord.Embed(title="   Invalid Command..",description="do ``$help`` to see all commands and command groups.", color=constants.EXCEPTION_COLOR)
            await message.reply(embed=embed)


singletons.client.run(os.getenv("econtoken"))



from commands.display.interactables import interactable

class BlackJackGame(interactable.interactable):
    def __init__(self, original_user, timeout=360):
        super().__init__(original_user=original_user, timeout=timeout)
    
    @discord.ui.button(label="<<", style=discord.ButtonStyle.green)
    async def FirstButton(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

def blackjack(message : discord.Message) ->None:
    import random
    # TODO : generate the dealers hand (1 card face up, 1 card face down)
    dealer_hand = [random.randint(1,10)]
    # TODO : generate the user's hand (2 cards face up)
    player_hand = [random.randint(1,10), random.randint(1,10)]
    # DISPLAY BOARD
    print(f"DEALER : {dealer_hand[0]} {dealer_hand[1]}")
    # TODO : Check Win/loss
    if (player_hand[0] + player_hand[1]) == 21:
        # WIN()
        pass
    
    # TODO : Player turn (Player can hit any amount. or stand.)
    # TODO : Check Win/loss (If got blackjack)
    # DISPLAY BOARD
    # TODO : Flip dealer's card
    # TODO ? dealer has 16 or less, generate a third card.
    # TODO : Check Win/loss
    # DISPLAY BOARD
    # TODO : End Game