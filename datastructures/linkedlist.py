from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

        def __eq__(self, other):
            return self.data == other.data if isinstance(other, LinkedList.Node) else self.data == other


    def __init__(self, data_type: type = object) -> None:
        """Creates an empty linked list"""
        self.data_type:T = data_type
        self.head:LinkedList.Node = None
        self.tail:LinkedList.Node = None
        self.length:int = 0
        self.travel_node:LinkedList.Node = self.head




    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        """Creates a new linked list with a predetermined sequence"""
        for obj in sequence:
            if not isinstance(obj, data_type):
                raise TypeError("An object in the sequence is not of type data_type")

        list = LinkedList(data_type)

        for obj in sequence: 
            list.append(obj)
        
        return list




    def append(self, item: T) -> None:
        """Appends an object to the end of the linked list"""
        # raises typeError for incorrect type
        if not isinstance(item, self.data_type):
            raise TypeError("Item is of incorrect type for linked list.")
        
        # if the list is empty - head and tail equal item
        if self.empty:
            self.head = self.tail = LinkedList.Node(data = item)

        # else, Next value of current tail = item, new item becomes tail
        else: 
            item_node = LinkedList.Node(data = item, previous = self.tail)
            self.tail.next = item_node
            self.tail = item_node
            
        self.length += 1



    def prepend(self, item: T) -> None:
        """Appends an object at the beginning of the linked list"""

        # raises typerror if the item is of incorrect type
        if not isinstance(item, self.data_type):
            raise TypeError("Item is of incorrect type for linked list.")
        
        # item becomes both head and tail if list starts empty
        if self.empty:
            self.head = self.tail = LinkedList.Node(data = item)

        # otherwise, becomes previous value for current head and becomes new head
        else:
            item_node = LinkedList.Node(data = item, next = self.head)
            self.head.previous = item_node
            self.head = item_node
        
        self.length += 1


    def _traverse_list(self, target):
        """Traverses the list and returns first instance of target, or None if target not found"""
        travel = self.head

        while travel:
            if travel.data == target:
                return travel
            
            travel = travel.next
        
        return None


    def insert_before(self, target: T, item: T) -> None:
        """Inserts a given item BEFORE the first instance of target item in linked list"""

        # raises typeErrors
        if not isinstance(target, self.data_type):
            raise TypeError("Target is not of correct data_type for linked list")
        if not isinstance(item, self.data_type):
            raise TypeError("Item is not of correct data_type for linked list")

        # finds element in list 
        instance = self._traverse_list(target)
        
        # if target was not found in list, raises error
        if instance is None:
            raise ValueError("Target not in in linked list.")
        
        # otherwise, inserts item before the target
        else:
            # if target is head, calls prepend
            if instance == self.head:
                self.prepend(item)
            else:
                # inserting between travel item and travel.previous
                item_node = LinkedList.Node(data = item, next = instance, previous = instance.previous)
                instance.previous.next = item_node
                instance.previous = item_node
                self.length += 1




    def insert_after(self, target: T, item: T) -> None:
        """Inserts a given item AFTER the first instance of a target item in linked list"""

        # raise the typeerrors
        if not isinstance(target, self.data_type):
            raise TypeError("Target is not of correct data_type for linked list.")
        if not isinstance(item, self.data_type):
            raise TypeError("Target is not of correct data_type for linked list.")
        
        # finds target element 
        instance = self._traverse_list(target)

        # raises error if not there
        if instance is None:
            raise ValueError("Target not in linked list.")
        
        # otherwise, inserts item after the target
        else:
            # if target is tail, calls append
            if instance == self.tail:
                self.append(item)
            else:
                # inserting between instance and instance.next
                item_node = LinkedList.Node(data = item, next = instance.next, previous = instance)
                instance.next.previous = item_node
                instance.next = item_node
                self.length += 1




    def remove(self, item: T) -> None:
        """removes the first instance of item from the linked list"""

        if not isinstance(item, self.data_type):
           raise TypeError("Item is of incorrect data_type for linked list.")
        
        # finds the first instance of the item
        instance = self._traverse_list(item)

        if instance is None:
            raise ValueError("Item is not in linked list.")
        

        # checks if length is 1 - then just clears list
        if self.length == 1:
            self.clear()
        # if instance is at the head (no previous)
        if instance.previous == None:
            self.pop_front()
        # if instance is at tail (no next)
        elif instance.next == None:
            self.pop()
        else:
            # otherwise, just connects the two nodes on either side
            instance.previous.next = instance.next
            instance.next.previous = instance.previous
            self.length -=1






    def remove_all(self, item: T) -> None:
        """Removes all instances of an item within the linked list"""

        # keeps calling self.remove on the item, until it returns that the item isn't in the list
        # also, that method will raise the needed exceptionss

        while True:
            try:
                self.remove(item)
            except ValueError:
                return 


    def _empty_err(self):
        if self.length == 0:
            raise IndexError("Linked list is empty.")



    def pop(self) -> T:
        """removes and returns the value from the end of the list"""
        self._empty_err()
        
        final = self.tail
        
        if self.length == 1:
            self.clear()
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -=1

        return final



    def pop_front(self) -> T:
        """removes and returns the first value of the list"""
        self._empty_err()
        
        first = self.head

        if self.length == 1:
            self.clear()
        else:
            self.head = self.head.next
            self.head.previous = None
            self.length -=1

        return first
    



    @property
    def front(self) -> T:
        """returns the first value from the linked list"""
        self._empty_err()
        return self.head



    @property
    def back(self) -> T:
        """returns the last value from the linked list"""
        self._empty_err()
        return self.tail

    @property
    def empty(self) -> bool:
        """returns true if the linked list is empty, false otherwise"""
        return self.head == None and self.tail == None

    def __len__(self) -> int:
        """returns the number of items in the linked list"""
        return self.length

    def clear(self) -> None:
        """removes all items from the linked list"""
        self.head = None
        self.tail = None
        self.length = 0

    def __contains__(self, item: T) -> bool:
        """returns true if an item is in the list, false otherwise"""
        if not isinstance(item, self.data_type):
            raise TypeError("item is of incorrect instance for linked list")
        
        return self._traverse_list(item) != None

    def __iter__(self) -> ILinkedList[T]:
        """returns an interator for the list"""
        
        curr_node = self.head
        while curr_node:
            yield curr_node.data
            curr_node = curr_node.next




    def __next__(self) -> T:
        """returns the next item in the linked list"""
        if not self.travel_node:
            self.travel_node = self.head

        else:
            self.travel_node = self.travel_node.next

        if self.travel_node is None:
            raise StopIteration
        
        return self.travel_node
    


    
    def __reversed__(self) -> ILinkedList[T]:
        """returns a reversed version of the list"""
        reversed = LinkedList(data_type=self.data_type)

        if self.length != 0:
            curr_element = self.tail
            reversed.append(curr_element.data)
            while curr_element.previous:
                curr_element = curr_element.previous
                reversed.append(curr_element.data)

        return reversed

    
    def __eq__(self, other: object) -> bool:
        """returns true if two lists are equal in elements, false otherwise"""
        # no idea if this will work but hoping it calls the iterators and accesses each 
        # sequential element from each list at the same time
        if self.length != other.length or self.data_type != other.data_type:
            return False


        zippy = zip(self, other)

        for itemS, itemO in zippy:
            if itemS != itemO:
                return False
        
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.length}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
