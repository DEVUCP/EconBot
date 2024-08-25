import datetime


class EnergyBar:
    """Represents the energy bar of a user."""
    full_slot ="▰"
    empty_slot = "▱"
    max_energy : str # maximum energy the user can have.
    current_energy : int # current energy the user has.
    last_used : datetime.datetime # last time energy was used

    def __init__(self, max_energy : int = 10, current_energy : int = 10):
        self.max_energy = max_energy
        self.current_energy = current_energy
        self.last_used = datetime.datetime.now()
    
    def ReplenishEnergy(self):
        import utils

        replish_amount = 0
        time_dict = utils.GetTimeDelta(initial_time=self.last_used) # Time since last energy used.

        if time_dict["days"]:
            replish_amount = self.max_energy

        elif int(time_dict["hours"]) > 0:
            replish_amount = int(time_dict["hours"]*2)
            self.LastUsed()
            
        self.IncrEnergy(amount=replish_amount)

    def DecrEnergy(self, amount : int):
        """Decreases the energy by amount."""
        self.current_energy -= amount
        self.ClampEnergy()
        self.LastUsed()
        
    def IncrEnergy(self, amount : int):
        """Increases the energy by amount."""
        self.current_energy += amount
        self.ClampEnergy()
    
    def ClampEnergy(self):
        """Clamps current energy to 0 if negative and to max energy if exceeds it."""
        if self.current_energy > self.max_energy:
            self.current_energy = self.max_energy
        if self.current_energy < 0 :
            self.current_energy = 0

    def LastUsed(self):
        """Updates Last used."""
        self.last_used = datetime.datetime.now()

    def SetEnergy(self, new_energy : int):
        """Sets the energy to new_energy."""
        self.current_energy = new_energy
        if self.current_energy > self.max_energy:
            self.current_energy = self.max_energy

    def GetEnergyBar(self) -> str:
        """Returns String of energy bar slots."""
        # Replenish Energy Check
        self.ReplenishEnergy()
        energy_bar = ""
        for i in range(self.max_energy):
            if i < self.current_energy:
                energy_bar += " " + self.full_slot
            else:
                energy_bar += " " + self.empty_slot
        energy_bar += f" ( {self.current_energy} / {self.max_energy} )"

        return energy_bar

    def GetEnergy(self) -> int:
        """Returns the current energy."""
        # Replenish Energy Check
        self.ReplenishEnergy()
        return self.current_energy