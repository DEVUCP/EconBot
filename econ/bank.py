import enum
from econ.cards import bankcard

class BankAccount:
    
    class DepositStatus(enum.Enum):
        MAXED = -1
        FAILED = 0
        SUCCEEDED = 1
        DEPOSIT_MAXED = 2
    
    bank_card : bankcard.BankCard # Bank card that the account is linked to.
    cash_on_hand : float # Money that's avaliable for immediate use.
    deposit : float # Money thats safe, but not available for immediate use.

    from econ.cards import cards
    def __init__(self, cash : float = 0, dep : float = 0, bank_card : bankcard.BankCard = cards.StandardCard()) -> None:
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
    
    def WithdrawAmount(self, amount : float) -> None:
        """Withdraws amount from the bank account.
            Returns True if successful, False otherwise.
        """
        # Check if deposit is enough to withdraw.
        if amount <= self.deposit and amount > 0:
            self.cash_on_hand += amount
            self.deposit -= amount
            return True
        return False
    
    def IsCardMaxxed(self, amount=0) -> bool:
        """Returns True if the bank card is maxxed, False otherwise."""
        if self.bank_card.GetCardMax() == None: # If card has no max, then it is not maxed.
            return False
        if amount + self.deposit >= int(self.bank_card.GetCardMax()):
            return True
        else:
            return False

    def AddCash(self, cash: float) -> None:
        """Adds cash to the cash on hand."""
        self.cash_on_hand += cash

    def RemoveCash(self, cash: float) -> None:
        """Removes cash from the cash on hand."""
        self.cash_on_hand -= cash
    
    def AddDeposit(self, dep : float) -> None:
        """Adds deposit to the deposit."""
        self.deposit += dep
    
    def RemoveDeposit(self, dep : float) -> None:
        """Removes deposit from the deposit."""
        self.deposit -= dep

    def GetCashOnHand(self) -> float:
        """Returns the cash on hand."""
        return self.cash_on_hand
    
    def GetDeposit(self) -> float:
        """Returns the deposit."""
        return self.deposit

    def SetDeposit(self, newdep : float) -> None:
        """Sets the deposit.
            Returns False if newdep exceeds the max balance of the bank card, True otherwise.
        """
        if newdep > self.bank_card.GetCardMax():
            return False
        self.deposit = newdep
        return True

    def SetCashOnHand(self, newcash : float) -> None:
        """Sets the cash on hand"""
        self.cash_on_hand = newcash
