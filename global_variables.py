import discord


# Discord Essential variables
intents =  discord.Intents.all()
client = discord.Client(intents=intents)


user_dict = {} # 1067541126518677664: serverid, list[econessentials.User]
