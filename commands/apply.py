from econ.jobs import listings, jobs, job
import discord
from utils import FindUser, ReplyWithException

async def Apply(message : discord.Message, command):

    if len(command) < 2:
        await ReplyWithException(message=message,exception_msg="Please specify a job to apply for.", exception_desc="You can check the available jobs with the `$jobs` command.")
        return

    command.pop(0)

    listing = listings.GetListing()

    job = command[0]

    job = " ".join(command)
    
    if not IsJobInListing(job_name=job, listing=listing):
        await ReplyWithException(message=message,exception_msg="That job is not open or does not exist.", exception_desc="You can check the available jobs with the `$jobs` command.")
        return

    user = FindUser(uid=message.author.id, sid=message.guild.id)
    job = FindJob(job_name=job, listing=listing)

    if not MetRequirements(user_attr=user.attributes, job_req=job.GetRequirements()):
        await ReplyWithException(message=message,exception_msg="You do not meet the requirements for that job.", exception_desc="You can check the requirements for that job with the `$info <job_title>` command.")
        return
    
    user.occupation = jobs.jobs[job.GetName().lower()]
    embed = discord.Embed(
        title=f"You have applied for the job of {job.GetName()}!", 
        description=f"You will now be paid {job.GetHourlyPay()} per hour.", 
        color=discord.Color.green()
        )
    await message.reply(embed=embed)

def FindJob(job_name : str, listing : list) -> job.Job:
    for job in listing:
        if job.GetName().lower() == job_name.lower():
            return job
    return None


def IsJobInListing(job_name : str, listing : list) -> bool:
    for job in listing:
        if job.GetName().lower() == job_name.lower():
            return True
    return False

def MetRequirements(user_attr : dict, job_req : dict) -> bool:
    if job_req == None:
        return True
    
    for req_name, req_val in job_req.items():

        if user_attr[req_name].GetLevel() < req_val:
            return False
    return True