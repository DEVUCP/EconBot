import econessentials
import random
import singletons

class StandardCard(econessentials.BankCard):
    def __init__(self, name = "Standard Card", max_balance = 1250.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class SignatureCard(econessentials.BankCard):
    def __init__(self, name = "Signature Card", max_balance = 2500.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class SignatureSilverCard(econessentials.BankCard):
    def __init__(self, name = "Signature Silver Card", max_balance = 5000.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class SignatureGoldCard(econessentials.BankCard):
    def __init__(self, name = "Signature Gold Card", max_balance = 15000.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class SignaturePlatinumCard(econessentials.BankCard):
    def __init__(self, name = "Signature Platinum Card", max_balance = 30000.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class SignatureDiamondCard(econessentials.BankCard):
    def __init__(self, name = "Signature Diamond Card", max_balance = 100000.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class EliteCard(econessentials.BankCard):
    def __init__(self, name = "Elite Card", max_balance = 250000.00):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.

class KingCard(econessentials.BankCard):
    def __init__(self, name = "King Card", max_balance = None):
        super().__init__(name=name, max_balance=max_balance) # Initilize parent.