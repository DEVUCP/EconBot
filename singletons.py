import discord
from econ.items import items
from saveload import saveload
import datetime

# Discord Essential variables

start_time = datetime.datetime.now() # Start time of the bot

class Client(discord.Client):
    async def Save(self):
        # Save accounts before closing
        # saveload.SaveUserDict()
        print("Client disconnected.")

    async def close(self):
        # Perform cleanup before closing
        await self.Save()
        
        # Call the parent class's close method
        await super().close()


intents =  discord.Intents.all()
client = Client(intents=intents)


# Market
market = [
    items.ComplementBag(quantity=1),
    items.Coffee(quantity=1),
    items.EnergyDrink(quantity=1),
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
