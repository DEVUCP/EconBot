import discord
import constants
from utils import ReplyWithException
from econ.jobs import listings, job, jobs

async def DisplayJobs(message : discord.Message) -> None:
    """Displays the jobs."""
    jobs = listings.GetListing()
    embed = GetEmbedJobs(jobs)
    await message.reply(embed=embed)

async def DisplayJobInfo(message : discord.Message, command : list[str]) -> None:
    """Displays the job info."""

    if  len(command) < 1:
        await ReplyWithException(message=message, exception_msg="Please specify a job.")
        return
    
    command.pop(0) # Removes prefix and action
        
    job = " ".join(command)
    
    if job not in jobs.jobs.keys():
        await ReplyWithException(message=message, exception_msg="That job does not exist.",exception_desc="use `$jobs` to see all available jobs at the moment.")
        return
    
    embed = GetJobInfoEmbed(jobs.jobs[job])

    await message.reply(embed=embed)

def GetEmbedJobs(jobs : list[job.Job]) -> discord.Embed:
    """Returns an embed with the jobs."""
    embed = discord.Embed(title="Jobs", description="Here are the week's job listings.", color=0x00ff00)
    for job in jobs:
        # This condition is temporary.
        if job.GetName() in constants.easy_jobs:
            embed.add_field(name="Starter Jobs", value="Jobs easy to apply for right away.", inline=False) # Header
            embed.add_field(name="------------------", value="", inline=False) # Seperator
            embed.add_field(name=job.name, value=job.description, inline=True)
            embed.add_field(name=f"${job.hourly_pay}/hour", value="", inline=True)
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="------------------", value="", inline=False) # Seperator
        else:
            embed.add_field(name=job.name, value=job.description, inline=True)
            embed.add_field(name=f"${job.hourly_pay}/hour", value="", inline=True)
            embed.add_field(name="", value="", inline=False)

    return embed

def GetJobInfoEmbed(job : job.Job) -> discord.Embed:
    """Returns an embed with the job info."""
    embed = discord.Embed(title=job.name, description=f"${job.hourly_pay}/hour", color=0x00ff00)
    embed.add_field(name="", value=job.description, inline=True)
    embed.add_field(name="Requirements", value="", inline=False)
    for requirement in job.requirements:
        embed.add_field(name=requirement, value=job.requirements[requirement], inline=True)
    return embed
