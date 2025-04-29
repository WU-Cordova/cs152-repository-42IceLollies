from projects.project3.drink import Drink
from datastructures.array import Array
from datastructures.linkedlist import LinkedList

class CustomerOrder:
    
    def __init__(self, name: str) -> None:
        """Initiates a Customer's order, starting with the given name for order, drinks to be added later)"""
        self._name: str = name
     
        self._drinks: LinkedList[Drink] = LinkedList(data_type=Drink)
        self._price: float = 0


    
    def add_drink(self, new_drink: Drink, customizations: str)-> None:
        """Adds a new drink to the running order and adds the price to the total"""
        new_drink.customization=customizations
        self._drinks.append(new_drink)
        self._price += new_drink.price


    def remove_drink(self, drink_name: Drink) -> None:
        """Removes the first instance of a given drink and price from the order, given its name"""
        for drink in self._drinks:
            if drink.name == drink_name:
                self._drinks.remove(drink)
                self._price -= drink.price
                return
            
        self.remove_drink(input("Drink not found in order, please enter another: "))
    


    def __iter__(self):
        """iterates through the drinks in the order"""
        for drink in self._drinks:
            yield drink
        

    @property
    def name(self) -> str:
        """returns the name property for an order"""
        return self._name


    def __str__(self) -> str:
        """Returns a string representation of the Customer's order"""
        formatted_price:str = "{:.2f}".format(self._price)
        return f"Here's what we have for your order: \n Name: {self._name} \n Order: {", ".join([str(d) for d in self._drinks])}\n Total: ${formatted_price}"
    
    def simple_str(self) -> str:
        """Returns a more simplified string representation of the order"""
        return f"{self._name}  -----  {", ".join([str(d) for d in self._drinks])}"
    

    