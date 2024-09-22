from utils import GetFilePath

PREFIX = "%"
SAVE_INTERVAL = 600 # in seconds
CRIME_FAIL_PERCENTAGE = 65 # chance of failing a crime


SETTINGS_PATH = GetFilePath(filename="settings.json")

PAGE_LEN = 5 # Max number of items in a market page
LISTING_LEN = 5 # Max number of job listings
LISTING_UPDATE_TIME = 7 # Time in-game days for the listing to update (24 mins * 7 = real world time)
EXCEPTION_COLOR = 0xff0000 # Exception Embed color

# Toggleables
ENABLE_CRIME = True
ENABLE_BEG = True
ENABLE_JOBS = True
ENABLE_UNEMPLOYED_WORK = False
ENABLE_ROB = True
AUTOSAVE = True


# Market Item Costs
COMPLEMENT_BAG_COST = 5.0
ENERGY_DRINK_COST = 10.0
COFFEE_COST = 12.5
LOTTERY_TICKET_COST = 5.0

INSULT_BAG_COST = 2.5
ADDERAL_COST = 52.5

# Pay ranges

BEG_PAY = (0.5, 2.0)
CRIME_PAY = (50.0, 150.0)
CRIME_PENALTY = (-100.0, -50.0)
WORK_PAY = (15.0, 65.0)

# Job categories

# TODO : Add more job categories

easy_jobs = ["Janitor",] # TODO : Add more jobs to the list


COMMANDS = {
    "training":{
        "study": "Raises your intellect",
        "socalize": "Raises your charisma",
        "workout": "Raises your strength",
        "paint": "Raises your dexterity & creativity"
    },

    "earnings": {
        "description": f"Example: `{PREFIX}help Earnings`",
        "work": "Work to earn some money",
        "crime": "Commit a crime to earn money illegally",
        "beg": "Beg for money on the streets",
        "rob": f"Attempt to rob another user\n example : ``{PREFIX}rob @myfriend``",
    },

    "bank": {
        "description": f"Example: `{PREFIX}help Bank`",
        "deposit": f"Deposit money into your bank account\n example : ``{PREFIX}dep 500``",
        "withdraw": f"Withdraw money from your bank account\n example : ``{PREFIX}with 500``",
        "pay": f"Send money to another user\n example : ``{PREFIX}pay @myfriend 500``",
    },
    
    "user": {
        "description": f"Example: `{PREFIX}help User`",
        "profile": "View all your stats",
        "balance": "Check your current balance",
        "inventory": "View your inventory",
        "give": f"Give an item to another user\n example : ``{PREFIX}give @myfriend complement bag | 4``",
        "use": "Use an item from your inventory",
        "energy":"Displays energy bar",
    },

    "market": {
        "description": f"Example: `{PREFIX}help Market`",
        "shop": "View the available items in the shop",
        "buy": f"Purchase an item from the shop\n example : ``{PREFIX}buy complement bag | 4``",
        "sell": f"Sell an item from your inventory\n example : ``{PREFIX}sell complement bag | 4``",
    },
    "jobs":{
        "description": f"Example: `{PREFIX}help jobs`",
        "jobs": "Shows you all available jobs this (ingame) week",
        "apply": f"Applies for a specific job\n example : ``{PREFIX}apply Economist``",
        "info": f"Gives details on a specific job\n example : ``{PREFIX}info Economist``",
    },

    "misc": {
        "description": f"Example: `{PREFIX}help Misc`",
        "clock":"Dislpays current ingame time",

    },

    "operator": {
        "description": f"Example: `{PREFIX}help Operator`",
        "op": f"Makes a user an operator\n example : ``{PREFIX}op @myfriend``",
        "deop": f"Removes operator status from a user\n example : ``{PREFIX}deop @myfriend``",
        "save": f"Saves the database\n example : ``{PREFIX}save``",
        "addcash": f"Adds cash to a user\n example : ``{PREFIX}ac @myfriend 500``",
        "remcash": f"Removes cash from a user\n example : ``{PREFIX}rc @myfriend 500``",
        "adddeposit": f"Adds cash to a user's bank account\n example : ``{PREFIX}ad @myfriend 500``",
        "removedeposit": f"Removes cash from a user's bank account\n example : ``{PREFIX}rd @myfriend 500``",
    }
}
OUTCOMES_WORK = [
    "You found a hidden treasure chest at work and earned **$#**",
    "Your boss gave you a surprise bonus of **$#** for your hard work",
    "You discovered a new way to save the company money and got a reward of **$#**",
    "You won the office lottery and received **$#**",
    "You fixed the coffee machine and everyone chipped in to give you **$#**",
    "You found a winning scratch-off ticket in the break room and won **$#**",
    "You helped a colleague with a project and they gave you **$#** as a thank you",
    "You found some extra cash in the vending machine and kept it, earning **$#**",
    "You completed a big project ahead of schedule and received a bonus of **$#**",
    "You found a forgotten envelope with **$#** in your desk drawer",
    "You organized the office party and got a tip of **$#**",
    "You won the 'Employee of the Month' award and received **$#**",
    "You found a valuable item at work and sold it for **$#**",
    "You helped fix a major issue and got a reward of **$#**",
    "You found a stash of petty cash and took **$#**"
]

OUTCOMES_CRIME = [
    "You successfully hacked into a bank and stole **$#**",
    "You pulled off a heist and got away with **$#**",
    "You pickpocketed a wealthy businessman and got **$#**",
    "You sold some 'hot' merchandise and earned **$#**",
    "You ran a successful scam and made **$#**",
    "You robbed a convenience store and got away with **$#**",
    "You mugged a tourist and found **$#** in their wallet",
    "You broke into a car and found **$#** in the glove compartment",
    "You stole a bike and sold it for **$#**",
    "You ran a counterfeit money operation and made **$#**",
    "You robbed a jewelry store and got away with **$#**",
    "You hijacked a truck and sold the goods for **$#**",
    "You ran an illegal gambling ring and earned **$#**",
    "You stole a purse and found **$#** inside",
    "You broke into a warehouse and found **$#** worth of goods"
]

OUTCOMES_FAIL_CRIME = [
    "you were caught by the police and fined **$#**"
]

OUTCOMES_BEG = [
    "A kind stranger felt sorry for you and gave you **$#**",
    "You found **$#** in an old coat pocket while begging",
    "A generous passerby handed you **$#**",
    "You sang a song and someone gave you **$#** for your effort",
    "You found a wallet with **$#** inside",
    "A child gave you their allowance of **$#**",
    "You found some loose change on the ground worth **$#**",
    "A street performer shared their earnings with you, giving you **$#**",
    "A tourist felt generous and gave you **$#**",
    "A dog walker gave you some spare change worth **$#**",
    "You found a hidden stash of coins worth **$#**",
    "A busker gave you a portion of their earnings, totaling **$#**",
    "You found a $5 bill stuck in a bush",
    "A kind soul bought you a meal and gave you **$#**"
]
OUTCOMES_WORKOUT = [
    "You went to the gym and worked out for an hour. You feel stronger and more confident.",
    "You went for a run and burned some calories. You feel energized and refreshed.",
    "You went for a swim and felt invigorated and relaxed.",
    "You went for a hike and felt connected with nature and accomplished.",
    "You went for a bike ride and felt exhilarated and free.",
    "You went for a yoga session and felt centered and balanced.",
    "You went for a dance class and felt joyful and expressive.",
    "You went for a martial arts class and felt disciplined and focused.",
    ]

OUTCOMES_STUDY = [
    "You studied for an hour and feel more knowledgeable and confident.",
    "You read a book and gained new insights and perspectives.",
    "You attended a lecture and learned something new and interesting.",
    "You practiced a skill and felt more skilled and capable.",
    "You attended a workshop and gained new skills and knowledge.",
    "You watched a documentary and learned something new and interesting.",
    "You attended a seminar and gained new insights and perspectives.",
    ]

OUTCOMES_PAINT = [
    "You painted a beautiful landscape and felt inspired and creative.",
    "You sketched a portrait and felt connected and expressive.",
    "You created an abstract piece and felt free and experimental.",
    "You painted a still life and felt focused and detailed.",
    "You drew a cartoon and felt playful and imaginative.",
    "You designed a logo and felt professional and creative.",
    "You created a digital artwork and felt tech-savvy and artistic.",
    "You painted a mural and felt impactful and creative.",
    ]

OUTCOMES_SOCIALIZE = [
    "You attended a networking event and made new connections and friends.",
    "You gave a speech and inspired and motivated others.",
    "You hosted a party and made people feel welcome and included.",
    "You volunteered at a charity event and made a difference in the community.",
    "You mentored a colleague and helped them grow and succeed.",
    "You led a team project and motivated and empowered your team.",
    "You mediated a conflict and helped find a peaceful resolution.",
    "You negotiated a deal and reached a win-win agreement.",
    ]

OUTCOMES_MEDITATE = [
    "You meditated for an hour and felt calm and centered.",
    "You practiced mindfulness and felt present and aware.",
    "You did a body scan and felt relaxed and grounded.",
    "You focused on your breath and felt peaceful and focused.",
    "You visualized a peaceful place and felt serene and tranquil.",
    "You practiced loving-kindness and felt compassionate and connected.",
    "You did a walking meditation and felt mindful and aware.",
    "You practiced gratitude and felt thankful and appreciative.",
    ]