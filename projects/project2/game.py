from projects.project2.grid import Grid
from projects.project2.cell import Cell
from projects.project2.kbhit import KBHit
import random
import time


class Game:

    def __init__(self, width: int = 10, height: int=10, starter_file: list[list[bool]]=[]) -> None:
        """Creates a game object to run game of life based on optional starter grid, width and height (without arguments, creates random grid)"""
        self.__width = width
        self.__height = height

        # Iterates game and asks user if they want to replay when it ends
        while(True):
            # starts grid from file or randomly
            if len(starter_file)==0:
                self.__grid = Grid([[Cell(random.choice([True, False])) for _ in range(self.__width)] for _ in range(self.__height)])
            else:
                self.__grid = Grid([[Cell(starter_file[i][j]) for i in range(self.__height)] for j in range(self.__width)])
            self.__grid.draw()
            self.__animate()

            action = input("Enter 'Q' to quit, or any other key to run again: ")
            if action == 'Q' or action == 'q':
                break

            


    def __animate(self) -> None:
        # creates a keyboard hit object to detect key presses
        kb = KBHit()
        print("Press enter to advance generation \n'A' to enter automatic mode (fast) \n'a' to enter automatic mode (slow) \n'Q' to quit")

        # unicode val of most recently pressed key
        key = 0
        # if game is in automatic mode and time between animation
        automatic = False
        timeout = 1

        # while not Q or q (quit condition) or stagnated board
        while key not in (81,113) and not self.__grid.get_stagnate():

            # reads key and converts to ASCII
            if kb.kbhit():
                key = ord(kb.getch())

                # if the key is A
                if key ==65:
                # sets automatic to True - fast mode
                    automatic = True
                    timeout = 0.5
                #  if the key is a
                # sets automatic to True - slow mode
                if key == 97:
                    automatic = True
                    timeout = 1
                
                # if enter is hit
                # sets automatic to false, advances generation
                if key == 13:
                    automatic = False
                    self.__grid.new_generation()
                    self.__grid.test_stagnation()

    
            
            if automatic:
                # automatic mode
                self.__grid.new_generation()
                self.__grid.test_stagnation()
                time.sleep(timeout)



        kb.set_normal_term()




    


