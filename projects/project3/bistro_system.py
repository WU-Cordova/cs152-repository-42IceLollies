from datastructures.deque import Deque
from datastructures.array import Array
from datastructures.bag import Bag
from projects.project3.customer_order import CustomerOrder
from projects.project3.menu import Menu, bistro_menu
import time
from projects.project3.drink import Drink

class Bistro_System:
    
    def __init__(self) -> None:
        self._open_orders:Deque = Deque(data_type=CustomerOrder)
        self._finished_orders:Bag = Bag()


    
    def print_main_menu(self) -> int:
        """Prints the main menu for the bistro to the terminal with action options
        returns: the selected option by the user (integer)"""

        print("\n\n\nWelcome to the Bearcat Bistro!\n \n 1) Display Menu \n 2) Take New Order \n 3) View Open Orders \n 4) Mark Next Order as Complete \n 5) View End of Day Report \n 6) Exit\n")

        return int(input("Please enter the number for your choice: "))
    



    def take_order(self) -> None:
        """Takes the user's order, asking for name, and menu items to add, confirms order, and adds to list of open orders"""

        # starts a new order given name
        new_order:CustomerOrder = CustomerOrder(name = input("Name for order: "))
        # adds drinks to the order
        while (True):
            new_drink:str = input("Enter the number or name of menu item (press ENTER when finished, or type 'cancel' to quit order): ")               
             
            # breaks loop when entered
            if new_drink == "":
                break
                
            if new_drink == "cancel" or new_drink == "Cancel":
                return
            
            # adds the drink, or repeats prompt if typo/not on menu
            try:
                order:Drink = bistro_menu.order(str(new_drink) if len(new_drink)> 3 else int(new_drink))
                customization:str = input("Please briefly explain any desired customizations (ENTER for none): \n")
                customization = customization if customization != "" else None
                new_order.add_drink(order, customization)

            except ValueError:
                print("Item not found.")



        # Asks if the order is correct until user answers yes
        while(True):
            match(input(f"\n{str(new_order)}\nDoes this order look correct? (y/n) ")):
                case "y":
                    break

                # removes an item from the order, and allows to add a correction
                case "n":
                    incorrect_order:str = input("Enter name of incorrect item or 'cancel' to quit correction: ")
                    if incorrect_order == "cancel" or incorrect_order== "Cancel":
                        break
                    new_order.remove_drink(incorrect_order)
                    
                    # loops in the case that an invalid menu item was added
                    while(True): 
                        new_drink:str = input("Enter the number or name of correction: ")
                    
                        try:
                            order:Drink = bistro_menu.order(str(new_drink) if len(new_drink)> 3 else int(new_drink))
                            customization:str = input("Please briefly explain any desired customizations (ENTER for none): \n")
                            customization = customization if customization != "" else None
                            new_order.add_drink(order, customization)
                            break
                        except ValueError:
                            print("Item not found.")
        

        # finishes the order by adding it to the list of open orders
        self._open_orders.enqueue(new_order)
        print("\n\nOrder Placed!")
        time.sleep(1.5)






    def print_open_orders(self) -> None:
        input("\n\nUp Next: \n - " + "\n - ".join([order.simple_str() for order in self._open_orders])+"\n\nPress ENTER to return to Main Menu.\n\n\n")



    def complete_order(self) -> None:
        """marks the first first order in the queue as completed (moves it to completed orders)"""
        order:CustomerOrder = self._open_orders.dequeue()
        for drink in order:
            self._finished_orders.add(drink.name)
        print(f"\nOrder for {order.name} completed!")
        time.sleep(3)



    def print_day_stats(self) -> None:
        """Prints out a list of the drinks sold for a day and the money made"""
        total:int = 0
        print("\n\n\nEnd of Day Sales Report \n\nDrinks Sold:\n")
        for drink_tup in self._finished_orders.distinct_items():
            units:int = self._finished_orders.count(drink_tup)
            unit_price:float = bistro_menu.order(drink_tup).price
            print(f"{drink_tup}  x{units} --------- {"{:.2f}".format(unit_price*units)}" )
            total += unit_price*units
        print(f"\nTotal: ${"{:.2f}".format(total)}\n\n")

        input("Press ENTER to return to the main menu.")