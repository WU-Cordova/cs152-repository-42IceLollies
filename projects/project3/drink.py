from dataclasses import dataclass

@dataclass
class Drink:
    """Initializes drink objects from dataclass"""
    # if generic is true, the drink object is uncustomized (used for menu items)
    # if false, it is a specific order, so will have size and customization
    generic: bool
    name: str
    # size: str|list[str]
    price: float
    customization:str = None
    size: str = "M"

    def __str__(self) -> None:
        formatted_price:str = "{:.2f}".format(self.price)
        if self.generic:
            return f"{self.name} ----------- ${formatted_price} (M)"# ({", ".join(self.size)})"
        return f"Medium {self.name} with customization: {self.customization} (${formatted_price})"
    
    def __eq__(self, other) -> bool: 
        """returns True if two drinks are equal (have same name), false otherwise"""
        return self.name == other.name