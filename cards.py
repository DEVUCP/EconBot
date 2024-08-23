import econessentials
import random
import singletons
import discord

class StandardCard(econessentials.BankCard):
    def __init__(self, name="Standard Card", max_balance=1250.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/_standardcard.png?raw=true')

class SignatureCard(econessentials.BankCard):
    def __init__(self, name="Signature Card", max_balance=2500.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/signaturecard.png?raw=true')

class SilverCard(econessentials.BankCard):
    def __init__(self, name="Signature Silver Card", max_balance=5000.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/silvercard.png?raw=true')

class GoldCard(econessentials.BankCard):
    def __init__(self, name="Signature Gold Card", max_balance=15000.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/goldcard.png?raw=true')

class PlatinumCard(econessentials.BankCard):
    def __init__(self, name="Signature Platinum Card", max_balance=30000.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/platinumcard.png?raw=true')

class DiamondCard(econessentials.BankCard):
    def __init__(self, name="Signature Diamond Card", max_balance=100000.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/diamondcard.png?raw=true')

class KingCard(econessentials.BankCard):
    def __init__(self, name="King Card", max_balance=250000.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/kingcard.png?raw=true')

class EliteCard(econessentials.BankCard):
    def __init__(self, name="Elite Card", max_balance=None):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/elitecard.png?raw=true')


def FindCardIndex(card : econessentials.BankCard):
    """Returns the index of the card."""
    for i in range(len(cards)):
        if type(card) == type(cards[i]):
            return i

cards = [
    StandardCard(),
    SignatureCard(),
    SilverCard(),
    GoldCard(),
    PlatinumCard(),
    DiamondCard(),
    KingCard(),
    EliteCard()
]