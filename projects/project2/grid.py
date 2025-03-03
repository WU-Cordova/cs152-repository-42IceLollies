from projects.project2.cell import Cell
from datastructures.array2d import Array2D
from datastructures.array import Array
import copy

class Grid:

    def __init__(self,  start_config: list[list[bool]]):
        """creates a grid of cells"""
        self.width = len(start_config)
        self.height = len(start_config[0])
        
        self.array = Array2D(start_config, Cell)
        self.grid_history = Array([Grid() for _ in range(5)], Grid)
    

    def draw(self):
        """Prints out the grid with all its cells to the terminal"""
        for col in self.array:
            # creates a string with "O" for living cells and "X" for dead cells in each row of the grid
            row_str = []
            for cell in col:
                row_str.append("O") if cell.living else row_str.append("-")
            # prints out each row
            print("  ".join(row_str))
        
        print()
            

        

    def new_generation(self):
        """Calculates all the cell statuses for next generation, and creates a new current grid"""
        # loop through all the cells in the grid
        new_grid = copy.deepcopy(self.array)
        # neighbors = []

        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                live_neighbors = 0
                # prin
                # t(i,j)
                # checks if all orthoganal cells are alive as long as the index is in bounds
                if i-1 >=0 and self.array[i-1][j].get_living():
                    # print("left")
                    live_neighbors+=1
                if j-1>=0 and self.array[i][j-1].get_living():
                    # print("top")
                    live_neighbors +=1
                if i+1 < (len(self.array)) and self.array[i+1][j].get_living():
                    # print("right")
                    live_neighbors+=1
                if j+1 < (len(self.array[0])) and self.array[i][j+1].get_living():
                    # print("bottom")
                    live_neighbors +=1

                # print(live_neighbors)
                # neighbors.append(live_neighbors)
                # changes if a cell is living if the projected status is different from current 
                if self.array[i][j].project_living(live_neighbors) != self.array[i][j].get_living():
                    new_grid[i][j].toggle_living()
        
        # keeps the grid history to five boards and appends the current board 
        if len(self.grid_history) >= 5:      
            self.grid_history[0].remove()
        self.grid_history.append(self.array)

        self.array = new_grid
        # print(neighbors)
        self.draw()



                
                
                
                
    
    def test_stagnation(self):
        """"""

        for arr in :
            if self.array == arr: