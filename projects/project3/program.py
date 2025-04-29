from projects.project3.menu import Menu, bistro_menu
from projects.project3.drink import Drink
from projects.project3.customer_order import CustomerOrder
from projects.project3.bistro_system import Bistro_System
import time

def main():
    """Loops through actions to run the Bearcat Bistro System, until option 6 is selected to quit program"""
    
    bistro_sys:Bistro_System = Bistro_System()
    
    # list of actions, will be referenced by index number
    actions:list = [bistro_menu.print_menu, bistro_sys.take_order, bistro_sys.print_open_orders, bistro_sys.complete_order, bistro_sys.print_day_stats, quit]

    # main while loop - loops until user exits program
    while(True):

        # prints the menu, receives a response from the user, and executes the action associated with that response
        try:
            actions[bistro_sys.print_main_menu()-1]()
            print("\n\n")
        # if there is a typo, asks again
        except ValueError:
            print("\nERROR. Please enter your number numerically (e.g. 1, 2, 3, etc.)")
            time.sleep(2)



    


if __name__ == '__main__':
    main()
