from projects.project2.grid import Grid
from projects.project2.cell import Cell
from projects.project2.kbhit import KBHit
import random
import time


class Game:

    def __init__(self, width: int = 10, height: int=10, *starter_file: str) -> None:
        # Random start
        self.width = width
        self.height = height
        self.grid = Grid([[Cell(random.choice([True, False])) for _ in range(self.width)] for _ in range(self.height)])
        self.grid.draw()


    def animate(self):
        kb = KBHit()
        print("Press enter to advance generation \n'A' to enter automatic mode \n'Q' to quit")

        # unicode val of most recently pressed key
        key = 0
        automatic = False
        # while not Q or q
        while key not in (81,113):

            # reads key 
            if kb.kbhit():
                key = ord(kb.getch())

                # if the key is A
                if key in (65, 97):
                # sets automatic to True
                    automatic = True
                
                # if enter is hit
                # sets automatic to false, advances generation
                if key == 13:
                    automatic = False
                    self.grid.new_generation()

    
            # A, a
            if automatic:
                # automatic mode
                self.grid.new_generation()
                time.sleep(1)



        kb.set_normal_term()




    


