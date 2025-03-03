class Cell:
    """represents a square on the board that is either alive or dead"""

    def __init__(self, living:bool = False):
        self.living = living

    # @property
    # def living(self):
    #     """getter for if the cell is living"""
    #     return self.living
    def get_living(self):
        return self.living
    
    def toggle_living(self):
        """makes cell alive if it is not or dead if it is alive"""
        self.living = not self.living
    
    def project_living(self, live_neighbors: int):
        """based on number of live neighbors, returns if the cell will be alive or dead next generation"""
        if live_neighbors == 0 or live_neighbors == 1 or live_neighbors == 4: 
            return False
        if live_neighbors == 2:
            return self.living
        if live_neighbors == 3:
             return True
        
    def __eq__(self, other) -> bool:
        return self.living == other.get_living()
