from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

# COMMENTS 
# THROW ERRORS!!!!!!!
# Make the row class variables consistend (with leading underscores)


# ============================================================================================================================
    class Row(IArray2D.IRow[T]):
        """Row class to support double bracket index reference and 2D iteration"""
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: T) -> None:
            # Initializes a row object belonging to a given array
            self.num_columns = num_columns
            self.array = array
            self.row_index = row_index
            self.data_type = data_type


        def __map_index(self, col_idx: int) -> int:
            """returns one dimensional index given two dimensional coordinates"""
            return self.row_index * self.num_columns + col_idx

        def __getitem__(self, column_index: int) -> T:
            """returns the item at a point in the one dimensional array given 2D array coordinates"""
            if column_index >= self.num_columns:
                raise IndexError("Column index out of bounds >:P")
            return self.array[self.__map_index(column_index)]
        
        
        def __setitem__(self, column_index: int, value: T) -> None:
            """sets the item at a point in the one dimensional array given 2D array coordinates"""
            if column_index >= self.num_columns:
                raise IndexError("Column index out of bounds >:P")
            self.array[self.__map_index(column_index)] = value
        
        def __iter__(self) -> Iterator[T]:
            """Iterator of the row (returns object from a column)"""
            for col_idx in range(self.num_columns):
                yield self.array[self.__map_index(col_idx)]
        
        def __reversed__(self) -> Iterator[T]:
            """Reversed iterator of a row (returns object from a column but loops backwards)"""
            for col_idx in range(self.num_columns-1, -1, -1):
                yield self.array[self.__map_index(col_idx)]

        def __len__(self) -> int:
            """returns the number of columns in a 2D array"""
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self.array[self.__map_index(column_index)]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self.array[self.__map_index(column_index)]) for column_index in range(self.num_columns - 1)])}, {str(self.array[self.__map_index(self.num_columns - 1)])}]'


# =============================================================================================================================

    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        """Initializes an instance of the 2D array given initial sequence and data type"""

        # print(str(starting_sequence))
        # raise the value errors
        if not isinstance(starting_sequence, Sequence):
            # wrong data type
            raise ValueError("Starting sequence is not a sequence")
        for curr_sequence in starting_sequence:
            # if it's not a sequence
            if not isinstance(curr_sequence, Sequence):
                raise TypeError("Starting_sequence should contain items of type Sequence.")
            # raises error if the starting sequence is not square
            if len(curr_sequence) != len(starting_sequence[0]):
                raise ValueError("Elements of starting sequence are not all of the same length.")

        # instance variables
        self.__num_columns = len(starting_sequence[0])
        self.__num_rows = len(starting_sequence)
        self.__data_type = data_type
        self.__array = Array([data_type() for _ in range(self.__num_rows) for _ in range(self.__num_columns)], data_type = data_type)
        
        # Iterates through both dimensions of the two dimensional list and adds the elements to a linear array
        # (index for linear array)
        idx = 0
        for row in range(self.__num_rows):
            for col in range(self.__num_columns):
                elem = starting_sequence[row][col]
                if not isinstance(elem, data_type):
                    # raises TypeError if an element of the starting_sequence is of an incorrect type
                    raise ValueError("2D Array element of incorrect type.")
                self.__array[idx] = elem
                idx += 1

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        """Creates and returns an empty instance of the 2D array given its dimensions"""
        # creates a starting sequence of the data type and converts it into a 2D array
        start_seq = [[data_type() for _ in range(rows)] for _ in range(cols)]
        arr =  Array2D(starting_sequence = start_seq, data_type = data_type)
        # print(arr)
        return arr


    def __getitem__(self, row_index: int) -> Array2D.IRow[T]:
        """Handles the row index from boxy brackets to return element at a given index""" 
        if row_index >= self.__num_rows:
            raise IndexError("Row index out of bounds >:P")
        return self.Row(array = self.__array, row_index = row_index, num_columns = self.__num_columns, data_type = self.__data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        """Iterates through the rows of the array, references Row class which iterates cols"""
        for row_idx in range(self.__num_rows):
            yield self.Row.__iter__(self.Row(array = self.__array, row_index = row_idx, num_columns = self.__num_columns, data_type = self.__data_type))
    
    def __reversed__(self):
        """Iterates backwards through the rows of the array"""
        for row_idx in range(self.__num_rows -1, -1, -1):
            yield self.Row.__iter__(self.Row(array = self.__array, row_index = row_idx, num_columns = self.__num_columns, data_type = self.__data_type))
    
    def __len__(self): 
        """Returns a 2D array's number of columns"""
        return self.__num_columns
                                  
    def __str__(self) -> str:            
        return  str([[self.__array[row_idx * self.__num_columns + i] for i in range(self.__num_columns)]for row_idx in range(self.__num_rows)])
        # return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'
    
    
    def __eq__(self, other:Array2D) -> bool:
        """returns true if all elements of current array and another array are equal and dimensions are equal"""
        if self.__num_columns == len(other) and self.__num_rows == len(other[0]):
            for i in range(self.__num_columns):
                for j in range(self.__num_rows):
                    if self[i][j] != other[i][j]:
                        return False
            
            return True
        else:
            return False



if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')