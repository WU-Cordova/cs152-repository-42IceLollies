from typing import Any
import copy

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type: T =object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self.__circ_arr = Array(data_type=data_type, starting_sequence= [data_type() for _ in range(maxsize+1)])
        self.__max_size = maxsize
        self.__front = 0
        self.__rear = 0
        self.__data_type = data_type


    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        # array is full if the rear +1 is the front
        return (self.__rear +1)%(self.__max_size+1) == self.__front%(self.__max_size+1)


    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        # checks item type is correct,
        # checks if queue is full - when the rear value is one behind the front value
        if not isinstance(item, self.__data_type):
            raise TypeError("Provided item is of incorrect type for circular queue.")
        if self.full:
            raise IndexError("Circular queue is full, no more elements can be added")

        # otherwise, adds the object in the rear position
        else:
            self.__circ_arr[self.__rear] = item
            self.__rear += 1
            self.__rear = self.__rear % (self.__max_size + 1)

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self.__rear == self.__front


    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        # raises error for empty queue
        if self.empty:
            raise IndexError("Circular Queue is empty, cannot remove elements")
        
        else:
            # otherwise returns the element at the front, and excludes it from range of active values
            el= self.__circ_arr[self.__front]
            self.__front += 1
            self.__front = self.__front % (self.__max_size + 1)
            return el

    def clear(self) -> None:
        ''' Removes all items from the queue '''
        raise NotImplementedError

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        # raises error if the queue is empty
        if self.empty:
            raise IndexError("Queue is empty, no front element available")
        # otherwise, returns but does not exclude the first element
        else:
            return self.__circ_arr[self.__front]

   
    
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return self.__max_size
    


    def __len__(self) -> int:
        ''' Returns the number of items in the queue
    
            Returns:
                The number of items in the queue
        '''
        return (self.__rear - self.__front + self.__max_size + 1) % (self.__max_size+1)
    


    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The front and rear pointers are equal
                - The elements between the front and rear pointers are equal, even if they are in different positions
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        # returns false if the number of elements in the queues are different, if the data types are differend
        if len(self) != len(other):
            return False
        if not isinstance(other.front, self.__data_type):
            return False
       
        # copies the queues, and, starting at the front, pops elements off and compares them
        # if any elements are different, returns false
        self_arr = copy.deepcopy(self)
        other_arr = copy.deepcopy(other)

        while not self_arr.empty:
            if self_arr.dequeue() != other_arr.dequeue():
                return False
        
        # if all the elements are the same, returns True
        return True

    
    


    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        return str(self.__circ_arr)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self.__circ_arr)})'
                                  
