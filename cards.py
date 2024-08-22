import econessentials
import random
import singletons
import discord
from utils import GetEmbedBalance, FindUser


class CardView(discord.ui.View):

    def __init__(self, original_user, message, timeout=180):
        super().__init__(timeout=timeout)
        self.original_user = original_user
        self.message = message
        
    def IsOriginalUser(self, user : discord.User) -> bool:
        """Returns True if user is the same as the original user."""
        return user.id == self.original_user.id

    @discord.ui.button(label="Upgrade Card!", style=discord.ButtonStyle.green)
    async def UpgradeCard(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Checks if the original user.
        if not self.IsOriginalUser(user=interaction.user):
            return

        user = FindUser(uid=self.original_user.id, sid=self.message.guild.id)

        if user.bank_acc.GetDeposit() >= user.bank_acc.bank_card.GetCardMax():
            new_card_index = FindCardIndex(user.bank_acc.bank_card) + 1
        
    
            user.bank_acc.bank_card = cards[new_card_index]
            user.bank_acc.SetDeposit(newdep=0.0)

            embed = await GetEmbedBalance(user=user)
            await interaction.response.edit_message(embed=embed, view=None)

class StandardCard(econessentials.BankCard):
    def __init__(self, name="Standard Card", max_balance=1250.00):
        super().__init__(name=name, max_balance=max_balance, image_link='https://github.com/DEVUCP/EconBot/blob/dev-build/assets/standardcard.png?raw=true')

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