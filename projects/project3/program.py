# DOCSTRINGS
# DRINKS SHOULD HAVE SIZES BUT ONLY SIZE MEDIUM
# TYPEHINTS ON DECLARED VARS

from projects.project3.menu import Menu
from projects.project3.drink import Drink
from projects.project3.customer_order import CustomerOrder

def main():
    
    new_menu = Menu([Drink(True, "Black Hole", 5.00), Drink(True, "London Fog", 5.25), 
                    Drink(True, "Latte", 4.50), Drink(True, "Matcha", 5.50), Drink(True, "Hot Tea", 4.00)])
    # new_menu.print_menu()

    test_order = CustomerOrder(name= "Sophieophie", drinks = [new_menu.order("Latte")])
    print(test_order)



if __name__ == '__main__':
    main()
