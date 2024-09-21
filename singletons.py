import discord
from econ.items import items
from saveload import saveload
import datetime

def print_colored(text, color):
    colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "reset": "\033[0m"
    }
    print(f"{colors[color]}{text}{colors['reset']}")

# Discord Essential variables

start_time = datetime.datetime.now() # Start time of the bot

class Client(discord.Client):
    async def Save(self):
        # Save accounts before closing

        await saveload.SaveUserDict()

        print_colored("--- Client disconnected ---", "red")

        exit(0)
        
    async def close(self):
        # Perform cleanup before closing
        await self.async_cleanup()
        
        # Call the parent class's close method
        await super().close()

    async def async_cleanup(self):
        await self.Save()



intents =  discord.Intents.all()
client = Client(intents=intents)

# Full Item list
item_list = [
    items.ComplementBag(quantity=1),
    items.Coffee(quantity=1),
    items.EnergyDrink(quantity=1),
    items.LotteryTicket(quantity=1),
    items.InsultBag(quantity=1),
    items.Adderall(quantity=1),
]


# Market
market = [
    items.ComplementBag(quantity=1),
    items.Coffee(quantity=1),
    items.EnergyDrink(quantity=1),
    items.LotteryTicket(quantity=1)
]

market_pages = [
    [], # Page 0
]

# Black Market
black_market = [
    items.InsultBag(quantity=1),
    items.Adderall(quantity=1),
]

black_market_pages = [
    [], # Page 0
]

user_dict = {} # {serverid : list[user.User], serverid : list[user.User] }
