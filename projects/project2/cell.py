class Cell:
    """represents a square on the board that is either alive or dead"""

    def __init__(self, living:bool = False) -> None:
        """creates a cell object that represents a cell as either dead or alibe"""
        self.__living = living

  
    def get_living(self) -> bool:
        """Getter for object's living variable"""
        return self.__living
    
    def toggle_living(self) -> None:
        """makes cell alive if it is not or dead if it is alive"""
        self.__living = not self.__living
    
    def project_living(self, live_neighbors: int) -> bool:
        """based on number of live neighbors, returns if the cell will be alive or dead next generation"""
        if live_neighbors == 0 or live_neighbors == 1 or live_neighbors >=4: 
            return False
        if live_neighbors == 2:
            return self.__living
        if live_neighbors == 3:
             return True
        
    def __eq__(self, other) -> bool:
        """returns if two cells are equal to each other (same living status)"""
        return self.__living == other.get_living()
