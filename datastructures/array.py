# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        # raises an error in the case the passed in starting_sequence isn't actually a sequence
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting_sequence is not of type Sequence.")

        # raises an error if the data_type is not a valid data type
        if not isinstance(data_type, type):
            raise ValueError("Data_type is not a valid type.")

        # raises an error if data in the starting_sequence is not the correct type
        for item in starting_sequence:
            if not isinstance(item, data_type):
                raise TypeError("Element of starting_sequence is of incorrect type.")

        self._elements = np.empty(len(starting_sequence), dtype = data_type)
        # adds all the starting elements to the array, copying the data directly
        self._elements= copy.deepcopy(starting_sequence)

        self._element_count = len(starting_sequence)
        self._capacity = len(starting_sequence) #is this right??? might be larger given a certain number of elements
        self._data_type = data_type



    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        """implements square bracket get operation"""

        # checks if a specific index is in the range of the array
        def in_range(i : int) -> bool:
            return i in range(-self._element_count, self._element_count)

        if isinstance(index, int):
            # if the index is within the range of array elements, return the item
            if in_range(index):
                item = self._elements[index]
                # if item is stored as a numpy generic, return via .item() method
                return item.item() if isinstance(item, np.generic) else item
            else:
                # otherwise, returns the fated error
                raise IndexError("Tee hee, index out of bounds. >:P")
            
        elif isinstance(index, slice):

            if in_range(index.start) and in_range(index.stop):
                return Array(starting_sequence=self._elements[index.start: index.stop: index.step], data_type = self._data_type)
        
        else:
            raise TypeError("Index should be an int or a slice")

    @property
    def empty(self):
        return len(self) == 0


    def __setitem__(self, index: int, item: T) -> None:
        """implements setting items with square bracket operator"""
        # returns error if index is out of bounds or the new item is the wrong datatype
        if not index in range(-self._element_count, self._element_count):
            raise IndexError("Tee hee, index out of bounds. >:P")

        if not isinstance(item, self._data_type):
            raise TypeError("New item is not of the correct type to be stored in this array.")

        # sets item
        self._elements[index] = item
        




    def append(self, data: T) -> None:
        """adds an element to the end of the array"""
        # perform resizing of memory size if necesary 
        if self._element_count == self._capacity:
            # creates an array with more memory space and adds it to the initial one
            expansion = np.array([self._data_type() for i in range(self._capacity)])
            print(expansion)
            self._elements = np.concatenate((self._elements, expansion))
            self._capacity*=2
        
        # appends the element, if it's the right type
        if not isinstance(data, self._data_type):
            raise ValueError("New element is of incorrect type.")
        
        self._elements[self._element_count] = data
        self._element_count += 1
    



    def append_front(self, data: T) -> None:
        """appends an item at the beginning of the array"""
        # first ensures the data is the correct type
        if not isinstance(data, self._data_type):
            raise ValueError("New element is of incorrect type")

        # checks if the array is at capacity and resizes accordingly if so
        if self._element_count == self._capacity:
            self._elements = np.concatenate((data, self._elements, np.array([0 for i in range(self._capacity -1)])))
            self._capacity*=2
            self._elements += 1
        
        else:
            for i in range(self.capacity-1,-1,-1):
                self._elements[i] = self._elements[i-1]
            self._elements[0] = data
            self._element_count += 1



    def __delitem__(self, index: int) -> None:
        """removes an item at a specific index from the array"""
        # if the array reaches a quarter of it's capacity, resizing time!
        if self._element_count-1 < self._capacity/4:
            self._capacity/=2
        # takes out the element
        self._element_count -=1
        self._elements = np.concatenate((self._elements[:index], self._elements[index+1:], [0 for i in range(self._capacity-self._element_count)]))

            


    def pop(self) -> None:
        """Deletes and returns the last item from an array"""
        item = self._elements[self._element_count-1]
        self.__delitem__(self._element_count-1)
        return item
    
    def pop_front(self) -> None:
        """Deletes and returns the first item from an array"""
        item = self._elements[0]
        self.__delitem__(0)
        return item



    def __len__(self) -> int: 
       """returns the number of elements in the array"""
       return self._element_count




    def __eq__(self, other: object) -> bool:
        """returns true if two arrays are equal in value"""
        # if they're not both arrays and one isn't the same length as the other, automatically neq 
        if not isinstance(other, Array) or len(other) != self._element_count:
                return False
        
        return all([(self._elements[i] == other[i]) for i in range(self._element_count)])



    
    def __iter__(self) -> Iterator[T]:
        """sequentially returns the elements of array"""
        for element in self._elements:
            yield element
    
    def index(self, target:T) -> int:
        """returns the index of a targetted value"""
        for el in range(len(self)):
            if self[el] == target:
                return el

        return -1


    def __reversed__(self) -> Iterator[T]:
        """returns iterated, reversed list"""
        reversed = Array(self._elements[:: -1], data_type=self._data_type)
        return iter(reversed)
    


    def __contains__(self, item: Any) -> bool:
        """returns true if the array contains a given item"""
        # first returns false automatically if the item is the wrong type
        if isinstance(item, self._data_type):
            return all([item in self._elements for i in range(self._element_count)])
        else:
            return False




    def clear(self) -> None:
        """Deletes all items from the list"""
        self._elements = Array([], self._data_type)
        self._element_count = 0
        self._capacity = 0



    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self._element_count}, Physical: {len(self._elements)}, type: {self._data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')