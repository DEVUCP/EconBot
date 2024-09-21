# Libraries
import discord
import os

import singletons
import constants
import utils

from saveload import saveload
from econ.jobs import listings

import commands

import startup

from commands import bank, earnings, inventory, display, training, apply, operator
from commands.display import balance, markets, inventory, clock, energy, help, profile, jobs
from commands.operator import permissions, management
from commands.earnings import work, crime, rob, beg


# Client Event Functions
@singletons.client.event
async def on_ready():
    
    await startup.StartUp()

@singletons.client.event
async def on_message(message : discord.Message):

    if message.author.id == singletons.client.user.id: # This ignores bot's own messages.
        return
    if len(message.content) == 0: # This ignores any gif or image messages.
        return

    if message.content[0] == constants.PREFIX:
        await InvokeEcon(message=message)

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
        case "prof":
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
            if constants.ENABLE_JOBS and constants.ENABLE_UNEMPLOYED_WORK:
                await commands.earnings.work.Work(message=message)
                
            elif constants.ENABLE_JOBS and not constants.ENABLE_UNEMPLOYED_WORK:
                await commands.earnings.work.JobOnlyWork(message=message)
            
            elif not constants.ENABLE_JOBS and constants.ENABLE_UNEMPLOYED_WORK:
                await commands.earnings.work.WorkNoJob(message=message)
            else:
                await utils.ReplyWithException(message=message, exception_msg="Conflicting setting! Notify Bot operator.", exception_desc="Jobs and Unemployed work are **both** disabled.")
        
        case "crime":
            if not constants.ENABLE_CRIME:
                return
            await commands.earnings.crime.Crime(message=message)
        case "beg":
            if not constants.ENABLE_BEG:
                return
            await commands.earnings.beg.Beg(message=message)
        case "rob":
            if not constants.ENABLE_ROB:
                return
            await commands.earnings.rob.Rob(message=message)
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
            if constants.ENABLE_JOBS:
                await commands.display.jobs.DisplayJobs(message=message)
        case "apply":
            if constants.ENABLE_JOBS:
                await commands.apply.Apply(message=message, command=command)
        case "info":
            if constants.ENABLE_JOBS:
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
        case "give":
           await commands.inventory.Give(message=message, command=command)
        case "clock":
            await commands.display.clock.DisplayClock(message=message)
        case "energy":
            await commands.display.energy.DisplayEnergy(message=message)
        case "operator":
            await commands.operator.permissions.AddOperator(message=message, command=command)
        case "op":
            await commands.operator.permissions.AddOperator(message=message, command=command)
        case "deop":
            await commands.operator.permissions.RemoveOperator(message=message, command=command)
        case "save":
            await commands.operator.management.ManualSave(message=message)
        case _: # None of the above.
            embed = discord.Embed(title="   Invalid Command..",description=f"do ``{constants.PREFIX}help`` to see all commands and command groups.", color=constants.EXCEPTION_COLOR)
            await message.reply(embed=embed)


singletons.client.run(os.getenv("econtoken"))
