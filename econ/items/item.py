
class Item:
    name : str
    description : str
    quantity : int
    cost : float

    def __init__(self, quantity : int, cost : float):
        self.quantity = quantity
        self.cost = cost
    from econ import user
    def Use(self, user : user.User) -> any:
        """Uses the item."""
        use = self.CustomUse(user) # Custom use for each item.

        self.DecrQuantity()
        
        return use

    def CustomUse(self, user : user.User) -> None:
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
