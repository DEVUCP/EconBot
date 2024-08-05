import econessentials
import random
import singletons

# All items

class InsultBag(econessentials.Item):
    insults = [
        "You suck.",
        "You smell bad.",
        "You are uninteresting.",
    ] # add funny insult lists

    name = "Insult Bag"
    description="Feeling too happy? This will definitely fix that!"
    
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=singletons.INSULT_BAG_COST) # Initilize parent.
    
    def CustomUse(self, user : econessentials.User) -> str:
        return random.choice(self.insults)

class ComplementBag(econessentials.Item):
    complements = [
        "You Rock!",
        "You smell great!",
        "You are a very interesting person!",
    ] # add funny complement lists

    name = "Complement Bag"
    description="Feeling too sad? This will definitely fix that!"
    
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=singletons.COMPLEMENT_BAG_COST) # Initilize parent.
    
    def CustomUse(self, user : econessentials.User) -> str:
        return random.choice(self.complements)