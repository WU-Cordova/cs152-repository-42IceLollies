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
        # object to detect kayboard hits and variable to store most recent key hit (by ASCII Value)
        self.__kb = KBHit()
        self.__key = -1
        self.__automatic = False
        self.__timeout = -1
        self.__iteration = 0


        # Iterates game and asks user if they want to replay when it ends
        while(True):
            # starts grid from file or randomly
            if len(starter_file)==0:
                self.__grid = Grid(0, [[Cell(random.choice([True, False])) for _ in range(self.__width)] for _ in range(self.__height)])
            else:            
                self.__grid = Grid(0, [[Cell(starter_file[j][i]) for i in range(self.__width)] for j in range(self.__height)])
            self.__grid.draw()
            self.__animate()

            if not self.__key in (81, 113): print("Press 'Q' to quit, or 'R' to run again: ")
            replay = False
            while(not replay):
                if self.__kb.kbhit():
                    self.__key = ord(self.__kb.getch())

                # if key is r or R, run again
                if self.__key in (82, 114):
                    self.__key = -1
                    replay = True
                # if key is q or Q, quit
                if self.__key in (81, 113):
                    quit()
            
        self.__kb.set_normal_term()
            


    def __animate(self) -> None:
        print("Press enter to advance generation \n'A' to enter automatic mode (fast) \n'a' to enter automatic mode (slow) \n'Q' to quit")

        # if game is in automatic mode and time between animation
        timeout = 1

        # while not Q or q (quit condition) or stagnated board
        while self.__key not in (81,113) and not self.__grid.get_stagnate() and self.__iteration < 100:

            # reads key and converts to ASCII
            if self.__kb.kbhit():
                self.__key = ord(self.__kb.getch())

                # if the key is A
                if self.__key ==65:
                # sets automatic to True - fast mode
                    self.__automatic = True
                    self.__timeout = 0.5
                #  if the key is a
                # sets automatic to True - slow mode
                if self.__key == 97:
                    self.__automatic = True
                    self.__timeout = 1
                
                # if enter is hit
                # sets automatic to false, advances generation
                if self.__key == 13:
                    self.__automatic = False
                    self.__grid.new_generation()
                    self.__grid.test_stagnation()
                    self.__iteration += 1

    
            
            if self.__automatic:
                # automatic mode
                self.__grid.new_generation()
                self.__grid.test_stagnation()
                self.__iteration += 1
                time.sleep(self.__timeout)




        




    


