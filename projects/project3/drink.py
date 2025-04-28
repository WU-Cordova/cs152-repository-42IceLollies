from dataclasses import dataclass

@dataclass
class Drink:
    # if generic is true, the drink object is uncustomized (used for menu items)
    # if false, it is a specific order, so will have size and customization
    generic: bool
    name: str
    # size: str|list[str]
    price: float
    customization:str = None

    def __str__(self) -> None:
        formatted_price = "{:.2f}".format(self.price)
        if self.generic:
            return f"{self.name} ----------- ${formatted_price}"# ({", ".join(self.size)})"
        return f"{self.name} with customization: {self.customization} (${formatted_price})"