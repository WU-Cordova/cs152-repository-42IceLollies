from dataclasses import dataclass

@dataclass
class Drink:
    # if generic is true, the drink object is uncustomized (used for menu items)
    # if false, it is a specific order, so will have size and customization
    generic: bool
    name: str
    size: str|list[str]
    price: float
    customization:str

    def __str__(self) -> None:
        if self.generic:
            return f"{self.name} ----------- ${self.price} ({[str(i)+',' for i in self.size]})"
        return f"Order: {self.size} {self.name} with customization: {self.customization} \n (${self.price})"