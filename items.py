import discord
import econessentials
import random

# All items
'''
Insult Bag

'''

class InsultBag(econessentials.Item):
    insults = [
        "You suck.",
        "You smell bad.",
        "You are uninteresting.",
    ] # add funny insult lists

    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(self, name="Insult Bag", quantity=quantity, cost=cost) # Initilize parent.
    
    def CustomUse(self, user : User) -> str:
        return random.choice(self.insults)