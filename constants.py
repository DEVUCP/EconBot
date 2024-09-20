PREFIX = "!"
SAVE_INTERVAL = 600 # in seconds

PAGE_LEN = 5 # Max number of items in a market page
LISTING_LEN = 5 # Max number of job listings
LISTING_UPDATE_TIME = 7 # Time in-game days for the listing to update (24 mins * 7 = real world time)
EXCEPTION_COLOR = 0xff0000 # Exception Embed color

# Market Item Costs
COMPLEMENT_BAG_COST = 5.0
ENERGY_DRINK_COST = 10.0
COFFEE_COST = 12.5
LOTTERY_TICKET_COST = 5.0

INSULT_BAG_COST = 2.5
ADDERAL_COST = 52.5

# Pay ranges

BEG_PAY = (0.5, 2.0)

# Job categories

easy_jobs = ["Janitor",]


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
}
OUTCOMES_WORK = {
    "You found a hidden treasure chest at work and earned **$#**": (2.0, 25),
    "Your boss gave you a surprise bonus of **$#** for your hard work": (100.0, 150.0),
    "You discovered a new way to save the company money and got a reward of **$#**": (75.0, 125.0),
    "You won the office lottery and received **$#**": (200.0, 300.0),
    "You fixed the coffee machine and everyone chipped in to give you **$#**": (20.0, 50.0),
    "You found a winning scratch-off ticket in the break room and won **$#**": (30.0, 60.0),
    "You helped a colleague with a project and they gave you **$#** as a thank you": (40.0, 80.0),
    "You found some extra cash in the vending machine and kept it, earning **$#**": (10.0, 25.0),
    "You completed a big project ahead of schedule and received a bonus of **$#**": (150.0, 250.0),
    "You found a forgotten envelope with **$#** in your desk drawer": (20.0, 40.0),
    "You organized the office party and got a tip of **$#**": (10.0, 30.0),
    "You won the 'Employee of the Month' award and received **$#**": (50.0, 100.0),
    "You found a valuable item at work and sold it for **$#**": (60.0, 120.0),
    "You helped fix a major issue and got a reward of **$#**": (80.0, 150.0),
    "You found a stash of petty cash and took **$#**": (5.0, 15.0)
}
OUTCOMES_CRIME = {
    "You successfully hacked into a bank and stole **$#**": (50.0, 100.0),
    "You pulled off a heist and got away with **$#**": (100.0, 150.0),
    "You pickpocketed a wealthy businessman and got **$#**": (30.0, 70.0),
    "You sold some 'hot' merchandise and earned **$#**": (80.0, 130.0),
    "You ran a successful scam and made **$#**": (60.0, 110.0),
    "You robbed a convenience store and got away with **$#**": (40.0, 90.0),
    "You mugged a tourist and found **$#** in their wallet": (20.0, 50.0),
    "You broke into a car and found **$#** in the glove compartment": (15.0, 35.0),
    "You stole a bike and sold it for **$#**": (25.0, 60.0),
    "You ran a counterfeit money operation and made **$#**": (70.0, 120.0),
    "You robbed a jewelry store and got away with **$#**": (200.0, 300.0),
    "You hijacked a truck and sold the goods for **$#**": (150.0, 250.0),
    "You ran an illegal gambling ring and earned **$#**": (100.0, 200.0),
    "You stole a purse and found **$#** inside": (10.0, 40.0),
    "You broke into a warehouse and found **$#** worth of goods": (80.0, 150.0)
}
OUTCOMES_BEG = {
    "A kind stranger felt sorry for you and gave you **$#**": BEG_PAY,
    "You found **$#** in an old coat pocket while begging": BEG_PAY,
    "A generous passerby handed you **$#**": BEG_PAY,
    "You sang a song and someone gave you **$#** for your effort": BEG_PAY,
    "You found a wallet with **$#** inside": BEG_PAY,
    "A child gave you their allowance of **$#**": BEG_PAY,
    "You found some loose change on the ground worth **$#**": BEG_PAY,
    "A street performer shared their earnings with you, giving you **$#**": BEG_PAY,
    "A tourist felt generous and gave you **$#**": BEG_PAY,
    "A dog walker gave you some spare change worth **$#**": BEG_PAY,
    "You found a hidden stash of coins worth **$#**": BEG_PAY,
    "A busker gave you a portion of their earnings, totaling **$#**": BEG_PAY,
    "You found a $5 bill stuck in a bush": BEG_PAY,
    "A kind soul bought you a meal and gave you **$#**": BEG_PAY
}
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