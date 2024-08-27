from econ import bank, energy
from econ.items import item
import constants

class User:
    uid : int # Unique ID of the user.
    bank_acc : bank.BankAccount
    networth : float
    energy : energy.EnergyBar
    inventory : list

    def __init__(self, uid) -> None:
        self.inventory = [[]]
        self.uid = uid
        self.bank_acc = bank.BankAccount()
        self.energy = energy.EnergyBar(max_energy=10, current_energy=10)
        self.networth = 0.0
    
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
        