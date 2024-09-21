import os
import singletons
import math
import constants
import pickle
import threading
import time
import asyncio
from utils import GetFilePath

loaded = False
save_task : asyncio.Task


save_path = GetFilePath(filename='saveload/userdata.pkl')

print(save_path)

async def timed_save(interval):
    while True:
        await asyncio.sleep(interval)
        print("Auto-Saving...")
        await SaveUserDict()

# Start the timed save in a separate thread

async def initiate_save():
    global save_task
    
    save_task = asyncio.create_task(timed_save(constants.SAVE_INTERVAL))


def LoadAll() -> bool:
    global loaded
    """Loads all data from files."""
    if not LoadUserDict():
        return False
    if not LoadMarketPages():
        return False
    if not LoadBlackMarketPages():
        return False
    loaded = True
    return True


async def SaveUserDict() -> None:
    try:
        with open(save_path, 'wb') as file:
            pickle.dump(singletons.user_dict, file=file)
            singletons.print_colored(". . . Saved Userdata Successfully !", "green")
    except Exception as err:
        print(f"Error: {err}")

def LoadUserDict() -> bool:
    if not os.path.exists(save_path):
        os.mknod(save_path)
    with open(save_path,'rb') as file:
       singletons.user_dict = pickle.load(file=file)
       return True

def LoadMarketPages() -> bool:
    """Loads market item list into market pages."""
    singletons.print_colored(f"[ LOADING MARKET . . . ]", "yellow")
    pages = math.ceil(len(singletons.market) / constants.PAGE_LEN)
    for i in range(pages):
        for j in range(constants.PAGE_LEN):
            try:
                singletons.market_pages[i].append(singletons.market[(constants.PAGE_LEN*i)+j])
            except IndexError:
                return True
            except Exception as e:
                print(e,singletons.market_pages[i])
                return False
        singletons.market_pages.append([]) # Adds new empty page list
    else:
        if singletons.market_pages[-1] == []:
            singletons.market_pages[-1].remove()
        singletons.print_colored(f"[ SUCCESSFULLY LOADED MARKET ! ]", "green")
        return True
    
def LoadBlackMarketPages() -> bool:
    """Loads blackmarket item list into blackmarket pages."""
    singletons.print_colored(f"[ LOADING BLACKMARKET . . . ] ", "yellow")
    pages = math.ceil(len(singletons.black_market) / constants.PAGE_LEN)
    for i in range(pages):
        for j in range(constants.PAGE_LEN):
            try:
                singletons.black_market_pages[i].append(singletons.black_market[(constants.PAGE_LEN*i)+j])
            except IndexError:
                return True
            except Exception as e:
                print(e,singletons.black_market_pages[i])
                return False
        singletons.black_market_pages.append([]) # Adds new empty page list
    else:
        if singletons.black_market_pages[-1] == []:
            singletons.black_market_pages[-1].remove()
        singletons.print_colored(f"[ SUCCESSFULLY LOADED BLACKMARKET ! ]", "green")
        return True
