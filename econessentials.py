import os
import discord


class BankAccount:
    cash_on_hand : float # Money that's avaliable for immediate use.
    deposit : float # Money thats safe, but not available for immediate use.

    def __init__(self, cash : float = 0, dep : float = 0):
        self.cash_on_hand = cash
        self.deposit = dep
    
    def DepositAmount(self, amount : float):
        # Check if cash on hand is enough to deposit.
        if amount <= self.cash_on_hand and amount > 0:
            self.deposit += amount
            self.cash_on_hand -= amount
    
    def WithdrawAmount(self, amount : float):
        # Check if deposit is enough to withdraw.
        if amount <= self.deposit and amount > 0:
            self.cash_on_hand += amount
            self.deposit -= amount
    
    def AddCash(self, cash: float):
        self.cash_on_hand += cash

    def RemoveCash(self, cash: float):
        self.cash_on_hand -= cash

    def GetCashOnHand(self) -> float:
        return self.cash_on_hand
    
    def GetDeposit(self) -> float:
        return self.deposit


    def SetDeposit(self, newdep : float):
        self.deposit = newdep

    def SetCashOnHand(self, newcash : float):
        self.cash_on_hand = newcash



class User:
    uid : discord.User.id #( int )
    bank_acc : BankAccount

    def __init__(self, uid) -> None:
        self.uid = uid
        self.bank_acc = BankAccount()
    

    


