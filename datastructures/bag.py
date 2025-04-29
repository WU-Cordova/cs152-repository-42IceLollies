from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """Initiates the bag object
        Arugments:
            items of type T: (optional) list of items to be instantiated in the bag
        Returns: 
            None
        """
        self.__bag__ = {}
        
        # if there is an interable 'items' provided
        if items != None:
            # loop through and adds all items to the bag
            for i in items:
                self.add(i)


    def add(self, item: T) -> None:
        """ adds items to a given bag object
        Arguments: 
            item of type T: the item to be added to the bag
        Returns: 
            None
        """
        if item is None:
            raise TypeError
        # if the same item is not yet in the bag, add it with count '1'
        else:
            if item not in self.__bag__:
                self.__bag__[item] = 1
                # otherwise, it adds one to the count of the items
            else:
                self.__bag__[item] += 1



    def remove(self, item: T) -> None:
        """Removes an instance of a given item from the bag, raises a value error if the item is not in the bag, or no item was specified
        Arguments: 
            item of type T: specified item to be removed from the bag
        Returns: 
            None
        """
        if item not in self.__bag__ or item is None:
            raise ValueError
        
        # if the number of items in the bag is greater than one, decreases the count
        if self.__bag__[item] > 1:
            self.__bag__[item] -= 1
        # otherwise, it takes the item out of the dictionary
        else:
            del self.__bag__[item]


    def count(self, item: T) -> int:
        """Returns the number of copies of an item stored as its value, zero if item is not in the bag
        Arguments:
            item of type T: the item that one is looking for in the bag
        Returns:
            int: number of copies of the given item in the bag"""
        try:
            count = self.__bag__[item]
            return count
        except KeyError:
            return 0
        

    def __len__(self) -> int:
        """Finds the total number of items currently stored in the bag
        Arguments:
            None
        Returns:
            int: number of itesm
        """
        len = 0
        for i in self.__bag__:
            len += self.__bag__[i]
        return len

    def distinct_items(self) -> Iterable[T]:
        """Returns a copy of all unique items in the bag
        Arguments:
            None
        Returns:
            Iterable[T]: iterable list of unique items
        """
        return self.__bag__.keys()

    def __contains__(self, item) -> bool:
        """Determines if an item is present inside the bag
        Arguments: 
            Item of type T: The object that may or may not be in the bag
        Returns:
            Boolean: True or False if the object is in the bag
        """
        return item in self.__bag__

    def clear(self) -> None:
        """Deletes all items inside the bag
        Arguments:
            None
        Returns:
            None
        """
        self.__bag__.clear()
        