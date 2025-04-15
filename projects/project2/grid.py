from projects.project2.cell import Cell
from datastructures.array2d import Array2D
import copy

class Grid:

    def __init__(self,  generation: int, start_config: list[list[Cell]]) -> None:
        """creates a grid of cells"""
        # starts from given congiguration or creates a blank board
        if start_config != None:        
            self.__array = Array2D(start_config, Cell)
        else:
            self.__array = Array2D.empty()

        self.__generation = generation
    # creates a grid history to test board stagnation
        self.__grid_history = []
        self.__stagnate = False
    

    def draw(self):
        """Prints out the grid with all its cells to the terminal"""

        print(f"Generation {self.__generation}:")

        for col in self.__array:
            # creates a string with "O" for living cells and "X" for dead cells in each row of the grid
            row_str = []
            for cell in col:
                row_str.append("O") if cell.get_living() else row_str.append("-")
            # prints out each row
            print("  ".join(row_str))
        
        print()



        

    def new_generation(self) -> None:
        """Calculates all the cell statuses for next generation, and creates a new current grid"""
        
        # loop through all the cells in the grid and makes changes where necessary for the next generation on a copy of the grid
        new_grid = copy.deepcopy(self.__array)
        self.__generation += 1

        for i in range(len(self.__array)):
            for j in range(len(self.__array[0])):
                live_neighbors = 0
                
                
                # alternative: try except w out of bounds, and use loops to check surrounding cells???


                # checks if all adjacent cells are alive as long as the index is in bounds
                out_of_bounds = []
                # checks if the top, right, left or bottom are out of bounds
                if j-1 <0: 
                    out_of_bounds.append("left")
                if i-1<0:
                    out_of_bounds.append("top")
                if j+1 >= (len(self.__array[0])):
                    out_of_bounds.append("right")
                if i+1 >= (len(self.__array)):
                    out_of_bounds.append("bottom")
                
                # checks top right, top and top left corners
                if not "top" in out_of_bounds:
                    if not "left" in out_of_bounds and self.__array[i-1][j-1].get_living():
                        live_neighbors+=1
                    if self.__array[i-1][j].get_living():
                        live_neighbors+=1
                    if not "right" in out_of_bounds and self.__array[i-1][j+1].get_living():
                        live_neighbors+=1

                # checks right corner
                if not "right" in out_of_bounds and self.__array[i][j+1].get_living():
                    live_neighbors+=1

                # checks left corner
                if not "left" in out_of_bounds and self.__array[i][j-1].get_living():
                    live_neighbors+=1

                # checks bottom right, bottom and bottom left corners
                if not "bottom" in out_of_bounds:
                    if not "left" in out_of_bounds and self.__array[i+1][j-1].get_living():
                        live_neighbors+=1
                    if self.__array[i+1][j].get_living():
                        live_neighbors+=1
                    if not "right" in out_of_bounds and self.__array[i+1][j+1].get_living():
                        live_neighbors+=1

              
                # changes if a cell is living if the projected status is different from current 
                if self.__array[i][j].project_living(live_neighbors) != self.__array[i][j].get_living():
                    new_grid[i][j].toggle_living()
        
        # keeps the grid history to five boards and appends the current board   
        if len(self.__grid_history) == 5:
            self.__grid_history.pop(0)
        self.__grid_history.append(self.__array)

        # sets current array to the new one and draws it
        self.__array = new_grid
        self.draw()


    def get_stagnate(self)-> bool:
        """getter for the stagnate variable"""
        return self.__stagnate
                
                
    
    def test_stagnation(self) -> None:
        """checks if the grid pattern is repeating and updates object's stagnate value"""

        if self.__array == self.__grid_history[len(self.__grid_history)-1]:
            self.__stagnate = True
            print(f"Game ended due to stability after {self.__generation} generations.")

        for arr in self.__grid_history:
            if self.__array == arr:
                self.__stagnate = True
                print(f"Game ended due to non_stable repeating after {self.__generation} generations.")

        