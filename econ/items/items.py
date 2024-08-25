from econ.items import item
import random
import constants

# All items

class InsultBag(item.Item):
    insults = [
        "You suck.",
        "You smell bad.",
        "You are uninteresting.",
    ] # add funny insult lists

    name = "Insult Bag"
    description="Feeling too happy? This will definitely fix that!"
    
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=constants.INSULT_BAG_COST) # Initilize parent.
    
    def CustomUse(self, user) -> str:
        return random.choice(self.insults)

class ComplementBag(item.Item):
    complements = [
        "You Rock!",
        "You smell great!",
        "You are a very interesting person!",
    ] # add funny complement lists

    name = "Complement Bag"
    description="Feeling too sad? This will definitely fix that!"
    
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=constants.COMPLEMENT_BAG_COST) # Initilize parent.
    
    def CustomUse(self, user) -> str:
        return random.choice(self.complements)
    
class Coffee(item.Item):
    name = "Coffee"
    description="Just another day at work."

    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=constants.COFFEE_COST) # Initilize parent.

    def CustomUse(self, user) -> str:
        user.energy.IncrEnergy(amount=1)
        return "Drank coffee. Energy increased by 1."

class EnergyDrink(item.Item):
    name = "Energy Drink"
    description="Not for the faint of heart."
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=constants.ENERGY_DRINK_COST) # Initilize parent.
    
    def CustomUse(self, user) -> str:
        user.energy.IncrEnergy(amount=2)
        return "Drank energy drink. Energy increased by 2."

class Adderall(item.Item):
    name = "Adderall"
    description="For those who need a little extra help."
    def __init__(self, quantity : int = 1, cost : float = 0):
        super().__init__(quantity=quantity, cost=constants.ADDERAL_COST) # Initilize parent.

    def CustomUse(self, user) -> str:
        user.energy.IncrEnergy(amount=3)
        return "Took adderall. Energy increased by 3."