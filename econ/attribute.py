

class Attribute:

    level : float # A float from 0% to 100%
    maximum = 100
    minimum = 0

    def __init__(self, level : float = 0.0, minimum : float = 0.0, maximum : float = 100.0) -> None:
        self.level = level
        self.minimum = minimum
        self.maximum = maximum

    def __str__(self) -> str:
        """Returns the attribute as a percentage."""
        return f"{self.level / self.maximum * 100}%"

    def IncrLevel(self, amount : float) -> None:
        """Increases the attribute by the given amount."""
        self.level += amount
        if self.IsMaxLevel():
            self.level = self.maximum

    def DecrLevel(self, amount : float) -> None:
        """Decreases the attribute by the given amount."""
        self.level -= amount
        if self.IsMinLevel():
            self.level = self.minimum

    def IsMaxLevel(self) -> bool:
        """Returns True if the attribute is at max level."""
        return self.level >= self.maximum
    
    def IsMinLevel(self) -> bool:
        """Returns True if the attribute is at min level."""
        return self.level <= self.minimum

    def GetLevel(self) -> float:
        """Returns the attribute as a percentage."""
        return self.level / self.maximum

    def SetLevel(self, attribute : float) -> None:
        """Sets the attribute to the given value."""
        self.level = attribute

    def GetLevelPercentage(self) -> float:
        """Returns the attribute as a percentage."""
        return self.level / self.maximum
