
class BankCard:
    name : str # Card title.
    max_balance : float # Maximum balance that can be deposited.
    image_link : str # link to image of card.

    def __init__(self, name : str, max_balance : float, image_link : str):
        self.name = name
        self.max_balance = max_balance
        self.image_link = image_link

    def GetCardImage(self) -> str:
        """Returns the image link of the card."""
        return self.image_link
    
    def GetCardMax(self) -> float:
        """Returns the max balance of the card."""
        return self.max_balance
    
    def GetCardName(self) -> str:
        """Returns the name of the card."""
        return self.name