import os

from datastructures.array import Array, T
from datastructures.istack import IStack
import copy

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.__arr_stack = Array(data_type = data_type, starting_sequence=[data_type() for i in range(max_size)])
        self.__top_idx = -1
        self.__max_size = max_size
        self.__data_type = data_type




    def push(self, item: T) -> None:
        """"If there is available space in the stack, adds the provided item to the top"""
        if self.__top_idx +1> self.__max_size:
            raise IndexError("Stack is full, cannot add new object.")
        else:
            self.__top_idx += 1
            self.__arr_stack[self.__top_idx] = item



    def pop(self) -> T:
        """returns the element at the end of the list and removes it from the stack"""
        # raises a value error if the stack is already empty
        if self.__top_idx == -1:
            raise IndexError("Array stack is empty, cannot remove elements.")
        
        # otherwise, return the element, and exclude it from the range of active elements
        element = self.__arr_stack[self.__top_idx]
        self.__top_idx -= 1
        return element



    def clear(self) -> None:
       """"removes all elements from the stack"""
    #    or at least sets the top index to -1 so they aren't accessible
       self.__top_idx = -1

    


    @property
    def peek(self) -> T:
       """returns value of the top value of the stack without removing it"""
       return self.__arr_stack[self.__top_idx]



    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return len(self.__arr_stack)
    


    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self.__top_idx == self.__max_size-1



    @property
    def empty(self) -> bool:
        """Returns true if the stack is empty, False otherwise"""
        return self.__top_idx == -1

    def __eq__(self, other: object) -> bool:
        """Returns True if the stack equals input stack (other), False otherwise"""
    #    checks they have the same number of elements first, and same data type
        if not self.__top_idx+1 == len(other):
            return False
        if self.__max_size != other.maxsize:
            return False
        if not isinstance(self.peek, type(other.peek)):
            return False

        # copies arrays and sees if all the elements are the same by popping them one by one
        self_arr = copy.deepcopy(self)
        other_arr = copy.deepcopy(other)

        while not self_arr.empty:
            if self_arr.pop() != other_arr.pop():
                return False
        
        # if len and all elements are equal, return True
        return True




    def __len__(self) -> int:
       """returns the number of elements currently in each array stack"""
       return self.__top_idx+1
    


    def __contains__(self, item: T) -> bool:
        # makes sure item is of correct time
        if not isinstance(item, self.__data_type):
            return False

        # copies the array stack and checks elements one by one, by popping off the top
        self_arr = copy.deepcopy(self)
        while not self_arr.empty:
               if self_arr.pop() == item:
                   return True
        return False



    def __str__(self) -> str:
        return str([self.__arr_stack[i] for i in range(self.__top_idx+1)])
    


    def __repr__(self) -> str:
        return f"ArrayStack({self.__max_size}): items: {str(self)}"
    

    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

