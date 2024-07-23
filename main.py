import discord
import os

intents =  discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("pleaseeeeeeeeeeeeeeeeeeeeeeeeee")

client.run(os.getenv("econtoken"))