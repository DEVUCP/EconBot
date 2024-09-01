import random
from econ.jobs import jobs, job
import constants
import datetime
from utils import GetTimeDelta


listing = []
last_updated = datetime.datetime.now()

def GenerateListings() -> None:
    """Generates a new listing."""
    global listing
    new_listing = []
    for i in range(constants.LISTING_LEN):

        new_job = random.choice(list(jobs.jobs.values())) # Generate a random job

        while new_job in new_listing: # If the job is already in the listing, generate a new one
            new_job = random.choice(list(jobs.jobs.values()))
        
        if new_job in new_listing: # If the job is already in the listing, generate a new one
            i-=1
            continue

        new_listing.append(new_job)

    listing = new_listing # Update the listing

def CheckUpdate() -> bool:
    """Checks if the listing needs to be updated."""
    global listing, last_updated
    time_since_update = GetTimeDelta(initial_time=last_updated) # Time since last listing update.

    if time_since_update["days"] > constants.LISTING_UPDATE_TIME:
        GenerateListings()
        last_updated = datetime.datetime.now()
        return True
    
    return False

def GetListing() -> list[job.Job]:
    global listing
    """Returns the listing."""
    CheckUpdate()
    return listing

def GetLastUpdated() -> datetime.datetime:
    """Returns the last updated time."""
    global last_updated
    return last_updated