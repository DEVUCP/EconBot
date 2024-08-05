import discord
import constants

class BankAccount:
    cash_on_hand : float # Money that's avaliable for immediate use.
    deposit : float # Money thats safe, but not available for immediate use.

    def __init__(self, cash : float = 0, dep : float = 0):
        self.cash_on_hand = cash
        self.deposit = dep
    
    def DepositAmount(self, amount : float):
        """Deposits amount into the bank account."""
        # Check if cash on hand is enough to deposit.
        if amount <= self.cash_on_hand and amount > 0:
            self.deposit += amount
            self.cash_on_hand -= amount
    
    def WithdrawAmount(self, amount : float):
        """Withdraws amount from the bank account."""
        # Check if deposit is enough to withdraw.
        if amount <= self.deposit and amount > 0:
            self.cash_on_hand += amount
            self.deposit -= amount
    
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
        """Sets the deposit"""
        self.deposit = newdep

    def SetCashOnHand(self, newcash : float):
        """Sets the cash on hand"""
        self.cash_on_hand = newcash


class User:
    uid : discord.User.id #( int )
    bank_acc : BankAccount
    inventory : list

    def __init__(self, uid) -> None:
        self.inventory = [[]]
        self.uid = uid
        self.bank_acc = BankAccount()
    
    def AddNewItemInventory(self, item) -> None:
        """Adds a new item to the inventory."""
        if len(self.inventory[-1]) == constants.PAGE_LEN:
            self.inventory.append([item])

        else:
            self.inventory[-1].append(item)

        
    
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


