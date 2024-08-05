import discord
import econessentials
import items


# Discord Essential variables
intents =  discord.Intents.all()
client = discord.Client(intents=intents)

# Market Item Costs
INSULT_BAG_COST = 150.0
COMPLEMENT_BAG_COST = 300.0

# Market
market = [
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.ComplementBag(quantity=1),
    items.InsultBag(quantity=1),
    items.InsultBag(quantity=1),
    items.InsultBag(quantity=1),
    items.InsultBag(quantity=1),
    items.InsultBag(quantity=1),
    ]

market_pages = [
    [], # Page 0
]

user_dict = {} # 1067541126518677664: serverid, list[econessentials.User]
