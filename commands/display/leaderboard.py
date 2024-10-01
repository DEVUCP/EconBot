import discord
import constants
import utils
import singletons

async def DisplayLeaderboard(message : discord.Message) -> None:
    """Displays the Leaderboard."""
    embed = discord.Embed(title="Leaderboard", description="The top 10 richest people in the server.")

    users = singletons.user_dict[message.guild.id]

    users = sorted(users, key=lambda user: user.networth, reverse=True)
    
    leng = len(users) if len(users) < 10 else 10
    for i in range(leng):
        user = users[i]
        u = await singletons.client.fetch_user(user.uid)
        embed.add_field(name=f"{i+1}. {u.display_name}", value=f"Networth: **{utils.ToMoney(user.networth)}**", inline=False)
    
    await message.reply(embed=embed)
    return