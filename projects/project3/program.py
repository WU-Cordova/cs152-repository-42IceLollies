from projects.project3.menu import Menu
from projects.project3.drink import Drink

def main():
    
    new_menu = Menu([Drink(True, "Drink1", ['M', 'L'], 2.45, None) for _ in range(5)])
    new_menu.print_menu()



if __name__ == '__main__':
    main()
