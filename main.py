import discord
import os

intents =  discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

client.run(os.getenv("econtoken"))