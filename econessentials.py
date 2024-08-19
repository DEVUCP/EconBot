import discord
import constants
import singletons
import datetime
import enum

class EnergyBar:
    """Represents the energy bar of a user."""
    full_slot ="▰"
    empty_slot = "▱"
    max_energy : str # maximum energy the user can have.
    current_energy : int # current energy the user has.
    last_used : datetime.datetime # last time energy was used

    def __init__(self, max_energy : int = 10, current_energy : int = 10):
        self.max_energy = max_energy
        self.current_energy = current_energy
        self.last_used = datetime.datetime.now()
    
    def ReplenishEnergy(self):
        import utils

        replish_amount = 0
        time_dict = utils.GetTimeDelta(initial_time=self.last_used) # Time since last energy used.

        if time_dict["days"]:
            replish_amount = self.max_energy

        elif int(time_dict["hours"]) > 0:
            replish_amount = int(time_dict["hours"]*2)
            self.LastUsed()
            
        self.IncrEnergy(amount=replish_amount)

    def DecrEnergy(self, amount : int):
        """Decreases the energy by amount."""
        self.current_energy -= amount
        self.ClampEnergy()
        self.LastUsed()
        
    def IncrEnergy(self, amount : int):
        """Increases the energy by amount."""
        self.current_energy += amount
        self.ClampEnergy()
    
    def ClampEnergy(self):
        """Clamps current energy to 0 if negative and to max energy if exceeds it."""
        if self.current_energy > self.max_energy:
            self.current_energy = self.max_energy
        if self.current_energy < 0 :
            self.current_energy = 0

    def LastUsed(self):
        """Updates Last used."""
        self.last_used = datetime.datetime.now()

    def SetEnergy(self, new_energy : int):
        """Sets the energy to new_energy."""
        self.current_energy = new_energy
        if self.current_energy > self.max_energy:
            self.current_energy = self.max_energy

    def GetEnergyBar(self) -> str:
        """Returns String of energy bar slots."""
        # Replenish Energy Check
        self.ReplenishEnergy()
        energy_bar = ""
        for i in range(self.max_energy):
            if i < self.current_energy:
                energy_bar += " " + self.full_slot
            else:
                energy_bar += " " + self.empty_slot
        energy_bar += f" ( {self.current_energy} / {self.max_energy} )"

        return energy_bar


    def GetEnergy(self) -> int:
        """Returns the current energy."""
        # Replenish Energy Check
        self.ReplenishEnergy()
        return self.current_energy

class BankCard:
    name : str # Card title.
    max_balance : float # Maximum balance that can be deposited.

    def __init__(self, name : str, max_balance : float):
        self.name = name
        self.max_balance = max_balance
    
    def GetCardMax(self) -> float:
        """Returns the max balance of the card."""
        return self.max_balance
    
    def GetCardName(self) -> str:
        """Returns the name of the card."""
        return self.name

class BankAccount:
    
    class DepositStatus(enum.Enum):
        MAXED = -1
        FAILED = 0
        SUCCEEDED = 1
        DEPOSIT_MAXED = 2
    
    bank_card : BankCard # Bank card that the account is linked to.
    cash_on_hand : float # Money that's avaliable for immediate use.
    deposit : float # Money thats safe, but not available for immediate use.

    import cards
    def __init__(self, cash : float = 0, dep : float = 0, bank_card : BankCard = cards.StandardCard()) -> None:
        self.cash_on_hand = cash
        self.deposit = dep
        self.bank_card = bank_card
    
    def DepositAmount(self, amount : float) -> int:
        """Deposits amount into the bank account.
            Returns True if successful, False otherwise.
        """
        # Check if cash on hand is enough to deposit.
        if self.IsCardMaxxed(amount=amount):
            amount = self.bank_card.GetCardMax() - self.deposit
            
            if amount <= 0:
                return -1
            
            self.deposit += amount
            self.cash_on_hand -= amount

            return 2
        if amount <= self.cash_on_hand and amount > 0:
            self.deposit += amount
            self.cash_on_hand -= amount
            return 1
        else:
            return 0  
    
    def WithdrawAmount(self, amount : float):
        """Withdraws amount from the bank account.
            Returns True if successful, False otherwise.
        """
        # Check if deposit is enough to withdraw.
        if amount <= self.deposit and amount > 0:
            self.cash_on_hand += amount
            self.deposit -= amount
            return True
        return False
    
    def IsCardMaxxed(self, amount) -> bool:
        """Returns True if the bank card is maxxed, False otherwise."""
        if amount + self.deposit > self.bank_card.GetCardMax():
            return True
        else:
            return False

    def AddCash(self, cash: float):
        """Adds cash to the cash on hand."""
        self.cash_on_hand += cash

    def RemoveCash(self, cash: float):
        """Removes cash from the cash on hand."""
        self.cash_on_hand -= cash

    def GetCashOnHand(self) -> float:
        """Returns the cash on hand."""
        return self.cash_on_hand
    
    def GetDeposit(self) -> float:
        """Returns the deposit."""
        return self.deposit

    def SetDeposit(self, newdep : float):
        """Sets the deposit.
            Returns False if newdep exceeds the max balance of the bank card, True otherwise.
        """
        if newdep > self.bank_card.GetCardMax():
            return False
        self.deposit = newdep
        return True

    def SetCashOnHand(self, newcash : float):
        """Sets the cash on hand"""
        self.cash_on_hand = newcash

class User:
    uid : discord.User.id #( int )
    bank_acc : BankAccount
    networth : float
    energy : EnergyBar
    inventory : list

    def __init__(self, uid) -> None:
        self.inventory = [[]]
        self.uid = uid
        self.bank_acc = BankAccount()
        self.energy = EnergyBar(max_energy=10, current_energy=10)
    
    def AddNewItemInventory(self, item) -> None:
        """Adds a new item to the inventory."""
        if len(self.inventory[-1]) == constants.PAGE_LEN:
            self.inventory.append([item])
        else:
            self.inventory[-1].append(item)

    def UpdateNetWorth(self) -> None:
        """Updates and sets the networth of the user."""
        networth = self.bank_acc.GetCashOnHand() + self.bank_acc.GetDeposit()
        for page in self.inventory:
            for item in page:
                networth += item.GetCost() * item.GetQuantity()
        self.SetNetWorth(networth=networth)
    
    def GetNetWorth(self) -> float:
        self.UpdateNetWorth()
        return self.networth
    
    def SetNetWorth(self, networth : float) -> None:
        self.networth = networth
        
    
class Item:
    name : str
    description : str
    quantity : int
    cost : float

    def __init__(self, quantity : int, cost : float):
        self.quantity = quantity
        self.cost = cost
    
    def Use(self, user : User) -> any:
        """Uses the item."""
        use = self.CustomUse(user) # Custom use for each item.

        self.DecrQuantity()
        
        return use

    def CustomUse(self, user : User) -> None:
        pass

    def DecrQuantity(self, decramount : int = 1): # Decrements quantity
        """Decrements the quantity of the item"""
        self.quantity -= decramount

    def IncrQuantity(self, incramount : int = 1): # Increments quantity
        """Increments the quantity of the item"""
        self.quantity += incramount

    def SetName(self, name : str):
        self.name = name    

    def SetQuantity(self, quantity : int):
        self.quantity = quantity

    def SetCost(self, cost : float):
        self.cost = cost        

    def GetName(self) -> str:
        return self.name
    
    def GetQuantity(self) -> int:
        return self.quantity
    
    def GetCost(self) -> float:
        return self.cost


