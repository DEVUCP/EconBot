
class Job:

    name : str
    hourly_pay : float
    description : str
    requirements : dict[str, float]

    def __init__(self, name : str, description : str, requirements : dict[str, float], hourly_pay : float = 0.0) -> None:
        self.name = name
        self.hourly_pay = hourly_pay
        self.description = description
        self.requirements = requirements

    def GetName() -> str:
        return self.name
    
    def GetDescription() -> str:
        return self.description
    
    def GetRequirements() -> dict[str, float]:
        return self.requirements
    
    def GetHourlyPay() -> float:
        return self.hourly_pay