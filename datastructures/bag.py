from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        """Initiates the bag object
        Arugments:
            items: (optional) list of items to be instantiated in the bag
        Returns: 
            void
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
            item: the item to be added to the bag
        Returns: 
            void
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
            item: specified item to be removed from the bag
        Returns: 
            void
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
            item: the item that one is looking for in the bag
        Returns:
            int: number of copies of the given item in the bag"""
        try:
            count = self.__bag__[item]
            return count
        except KeyError:
            return 0
        

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")