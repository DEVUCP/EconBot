import saveload
import singletons
import os
import json
import constants
import utils
from econ.jobs import listings
from saveload import saveload
import ast
from singletons import print_colored

settings = {}

invalid_prefixes = [
    " ",
    "",
    "/",
]

convert_old_save = False

async def StartUp() -> None:
    '''Inittializes and loads the bot.'''

    if LoadSettings():
        ApplySettings()
    
    GenerateHelpCommand()
    
    if constants.ENABLE_JOBS:
        listings.GenerateListings() # Generates the job listings

    await GenerateSaveFile() # Generates a save file if it does not exist.

    LoadUserData() # Loads the user data from the save file.

    saveload.LoadMarketPages()

    saveload.LoadBlackMarketPages()

    await StartAutoSave() # Starts the auto save thread.

    print_colored(f'--- LOGGED IN AS {singletons.client.user.name} ({singletons.client.user.id}) ---', 'magenta')

def GenerateHelpCommand():
    constants.COMMANDS = {
    "training":{
        "study": "Raises your intellect",
        "socalize": "Raises your charisma",
        "workout": "Raises your strength",
        "paint": "Raises your dexterity & creativity"
    },

    "earnings": {
        "description": f"Example: `{constants.PREFIX}help Earnings`",
        "work": "Work to earn some money",
        "crime": "Commit a crime to earn money illegally",
        "beg": "Beg for money on the streets",
        "rob": f"Attempt to rob another user\n example : ``{constants.PREFIX}rob @myfriend``",
    },

    "bank": {
        "description": f"Example: `{constants.PREFIX}help Bank`",
        "deposit": f"Deposit money into your bank account\n example : ``{constants.PREFIX}dep 500``",
        "withdraw": f"Withdraw money from your bank account\n example : ``{constants.PREFIX}with 500``",
        "pay": f"Send money to another user\n example : ``{constants.PREFIX}pay @myfriend 500``",
    },
    
    "user": {
        "description": f"Example: `{constants.PREFIX}help User`",
        "profile": "View all your stats",
        "balance": "Check your current balance",
        "inventory": "View your inventory",
        "give": f"Give an item to another user\n example : ``{constants.PREFIX}give @myfriend complement bag | 4``",
        "use": "Use an item from your inventory",
        "energy":"Displays energy bar",
    },

    "market": {
        "description": f"Example: `{constants.PREFIX}help Market`",
        "shop": "View the available items in the shop",
        "buy": f"Purchase an item from the shop\n example : ``{constants.PREFIX}buy complement bag | 4``",
        "sell": f"Sell an item from your inventory\n example : ``{constants.PREFIX}sell complement bag | 4``",
    },
    "jobs":{
        "description": f"Example: `{constants.PREFIX}help jobs`",
        "jobs": "Shows you all available jobs this (ingame) week",
        "apply": f"Applies for a specific job\n example : ``{constants.PREFIX}apply Economist``",
        "info": f"Gives details on a specific job\n example : ``{constants.PREFIX}info Economist``",
    },

    "gambling": {
        "description": f"Example: `{constants.PREFIX}help Gambling`",
        "slots": f"Play the slots game\n example : ``{constants.PREFIX}slots 100``",
        "blackjack": f"Play the blackjack game\n example : ``{constants.PREFIX}blackjack 10``",
        "roulette": f"Enter a roulette bet, you can bet on 3 different colors, or if the number will be even or odd, or you can bet on the exact number.\n example 1: ``{constants.PREFIX}roulette 130 green``\n example 2: ``{constants.PREFIX}roulette 120 31``\n example 3: ``{constants.PREFIX}roulette 50 even``"
    },

    "misc": {
        "description": f"Example: `{constants.PREFIX}help Misc`",
        "leaderboard": f"Shows the top 10 users with the highest networth\n example : ``{constants.PREFIX}leaderboard``",
        "clock":"Dislpays current ingame time",

    },

    "operator": {
        "description": f"Example: `{constants.PREFIX}help Operator`",
        "op": f"Makes a user an operator\n example : ``{constants.PREFIX}op @myfriend``",
        "deop": f"Removes operator status from a user\n example : ``{constants.PREFIX}deop @myfriend``",
        "save": f"Saves the database\n example : ``{constants.PREFIX}save``",
        "addcash": f"Adds cash to a user\n example : ``{constants.PREFIX}ac @myfriend 500``",
        "remcash": f"Removes cash from a user\n example : ``{constants.PREFIX}rc @myfriend 500``",
        "adddeposit": f"Adds cash to a user's bank account\n example : ``{constants.PREFIX}ad @myfriend 500``",
        "removedeposit": f"Removes cash from a user's bank account\n example : ``{constants.PREFIX}rd @myfriend 500``",
    }
}
    if not constants.ENABLE_JOBS:
        del constants.COMMANDS["jobs"]

    if not constants.ENABLE_BEG:
        del constants.COMMANDS["earnings"]["beg"]

    if not constants.ENABLE_CRIME:
        del constants.COMMANDS["earnings"]["crime"]
    
    if not constants.ENABLE_ROB:
        del constants.COMMANDS["earnings"]["rob"]

async def StartAutoSave() -> None:
    '''Starts the auto save thread.'''
    if constants.AUTOSAVE:
        print_colored("[ INITIATING AUTO-SAVE . . . ]", 'yellow')
        await saveload.initiate_save()

def LoadSettings() -> bool:
    '''Loads the settings from the settings.json file.'''
    global settings

    try:
        if os.path.exists(constants.SETTINGS_PATH):
            print_colored("[ SETTINGS FILE FOUND ]", "green")
            with open(constants.SETTINGS_PATH, 'r') as f:
                settings = json.load(f)
                return True
        else:
            print_colored("[ SETTINGS FILE NOT FOUND ]", "red")
            return False
    except Exception as e:
        print(f"!! Error loading settings: {e} !!")
        return False



def ValidSettings() -> bool:
    '''Validates the settings.'''
    global settings

    

    print_colored("[ VALIDATING SETTINGS . . . ]", "yellow")

    valid_prefix = IsValidPrefix(settings['general']['prefix'])
    print_colored(f"[ VALID PREFIX ]", "green") if valid_prefix else print_colored(f"!! INVALID PREFIX !!", "red")

    valid_autosave = IsValidAutosave(settings['general']['auto-save'])
    print_colored(f"[ VALID AUTOSAVE ]", "green") if valid_autosave else print_colored(f"!! INVALID AUTOSAVE !!", "red")

    valid_autosave_interval = IsValidSavingInterval(settings['general']['saving-interval'])
    print_colored(f"[ VALID SAVING INTERVAL ]", "green") if valid_autosave_interval else print_colored(f"!! INVALID SAVING INTERVAL !!", "red")

    for value in settings['game']['toggleables'].values():
        toggle_valid = IsValidToggleable(value)
        if not toggle_valid:
            print_colored(f"!! INVALID TOGGLEABLE !!", "red")
            print_colored("EXITING SETTINGS . . ." , "yellow")
            return False

    print_colored("[ VALID TOGGLEABLES ]", "green")

    for value in settings['game']['pay'].values():
        pay_valid = IsValidPay(value)
        if not pay_valid:
            print_colored(f"[!! INVALID PAY !!],", "red")
            print_colored("EXITING SETTINGS . . .", "yellow")
            return False
    
    print_colored("[ VALID PAY ]", "green")

    valid_job_listing_len = IsValidJobListingLen(settings['game']['job-listing-length'])

    print_colored(f"[ VALID JOB LISTING LENGTH ]", "green") if valid_job_listing_len else print_colored(f"!! INVALID JOB LISTING LENGTH !!", "red")

    all_valid = valid_prefix and valid_autosave and valid_autosave_interval and valid_job_listing_len

    return all_valid

def IsValidPrefix(prefix : any) -> bool:
    '''Checks if the prefix is valid.'''
    if not isinstance(prefix, str) or len(prefix) != 1 or prefix in invalid_prefixes:
        return False
    return True

def IsValidAutosave(autosave : any) -> bool:
    '''Checks if the autosave is valid.'''
    if not isinstance(autosave, bool):
        return False
    return True


def IsValidSavingInterval(saving_interval : any) -> bool:
    '''Checks if the saving interval is valid.'''
    if not isinstance(saving_interval, int) or saving_interval <= 5:
        return False
    return True

def IsValidToggleable(toggle : any) -> bool:
    '''Checks if the toggelable setting is valid.'''
    if not isinstance(toggle, bool):
        return False
    return True

def IsValidPay(pay_range : any) -> bool:
    '''Checks if the pay range is valid.'''
    if len(pay_range) != 2 or pay_range[0] > pay_range[1] or not isinstance(pay_range[0], float) or  not isinstance(pay_range[1], float):
        return False
    return True

def IsValidJobListingLen(job_listing_len : any) -> bool:
    '''Checks if the job listing length is valid.'''
    if not isinstance(job_listing_len, int) or job_listing_len <= 1:
        return False
    return True


def ApplySettings() -> None:
    '''Applies the settings to the bot.'''
    global settings, convert_old_save

    # Validate settings
    valid_settings = ValidSettings() # Returns a boolean value indicating whether the settings are valid.

    if not settings:
        return False

    if not valid_settings:
        print_colored("!!! INVALID SETTINGS !!!", "red")
        print("Please check the settings.json file . . .")
        return
    
    if settings['startup']['update-old-users']:
        convert_old_save = True
    
    constants.PREFIX = settings['general']['prefix']
    constants.AUTOSAVE = settings['general']['auto-save']
    constants.SAVE_INTERVAL = settings['general']['saving-interval']

    constants.ENABLE_CRIME = settings['game']['toggleables']['enable-crime']
    constants.ENABLE_BEG = settings['game']['toggleables']['enable-beg']
    constants.ENABLE_ROB = settings['game']['toggleables']['enable-rob']
    constants.ENABLE_JOBS = settings['game']['toggleables']['enable-jobs']
    constants.ENABLE_UNEMPLOYED_WORK = settings['game']['toggleables']['enable-unemployed-work']

    constants.BEG_PAY = settings['game']['pay']['beg-pay']
    constants.CRIME_PAY = settings['game']['pay']['crime-pay']
    constants.WORK_PAY = settings['game']['pay']['work-pay']

    constants.CRIME_FAIL_PERCENTAGE = settings['game']['crime-fail-percentage']

    constants.LISTING_LEN = settings['game']['job-listing-length']


async def GenerateSaveFile() -> None:
    '''Generates a save file if it does not exist.'''
    if not os.path.exists(saveload.save_path):
        print_colored("[ SAVE FILE NOT FOUND ]", "yellow")
        print_colored("[ GENERATING NEW SAVE FILE ]", "yellow")
        await saveload.SaveUserDict()
        print_colored("[ GENERATED SAVE FILE ]", "green")

def LoadUserData():
    '''Loads the user data from the save file.'''
    global convert_old_save
    if os.path.exists(saveload.save_path):
        saveload.LoadUserDict()

        #if convert_old_save:
            #print("[ CONVERTING OLD SAVE FILE ]")
            #await ConvertOldSave()

        print_colored("[ LOADED USER DATA ]",  "green")