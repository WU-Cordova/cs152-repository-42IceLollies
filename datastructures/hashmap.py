import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self.__buckets = Array([LinkedList(data_type=tuple) for _ in range(number_of_buckets)], data_type=LinkedList)
        self.__load_factor = load_factor
        self.__hash_func = custom_hash_function if custom_hash_function else self._default_hash_function
        self.__num_buckets = number_of_buckets
        self.__full_buckets = 0

    # array of linked lists of tuples (key, val)
    # hash func should be class var
    # get key value pair func


    def __get_bucket(self, key:KT) -> Array:
        """returns the index for a bucket using the hash function"""
        return self.__hash_func(key) % self.__num_buckets


    def __find_key_val_pair(self, key:KT)-> tuple:
        """returns the index within a bucket of a key-value-pair if it exists in the buckets, otherwise returns None"""
        # finds the bucket the value would exist in 
        bucket = self.__get_bucket(key)
        for item in self.__buckets[bucket]:
            if item[0] == key:
                return item
        
        raise KeyError("There is no such object in hashmap.")
       




    def __getitem__(self, key: KT) -> VT:
        # returns the value associated with a key, raising an error if the key is not found
        return self.__find_key_val_pair(key)[1]
    




    def __resize(self) -> None:
        """Checks whether the map has exceeded its load, and if it has, adds more buckets"""
               
        if self.__num_buckets * self.__load_factor <= self.__full_buckets:

            # number of buckets doubled
            doubled = 2* self.__num_buckets

            # recursive function determines if a number is prime
            def is_prime(num, div = 2):
                if div == int(num ** 0.5)+1:
                    return True
                
                if num % div == 0:
                    return False
                
                return is_prime(num, div +1)
            
            # loop searches for the next largest prime
            while not is_prime(doubled):
                doubled+=1

            new_bucket_ct = doubled

            # creates a new array for the hashmap and transfers current data over
            temp = Array([LinkedList(data_type=tuple) for _ in range(new_bucket_ct)], data_type=LinkedList)
            for b in range(len(self.__buckets)):
                for item in self.__buckets[b]:
                    temp[b].append(item)

            self.__buckets = temp




    def __setitem__(self, key: KT, value: VT) -> None: 
        # raise errs

        # not sure if this is meant to have a specific data type for the whole map/ how the incorrect data type is determined
        # if not isinstance(value, self.__data):
        #     pass
      
        # check if key is in map
        try:
            item = self.__find_key_val_pair(key)
            bucket = self.__buckets[self.__get_bucket(key)]
            bucket.replace(item,(key, value))
            
        except KeyError:
            
            # resize if necesasry
            self.__resize()

            # if not, add item to map
            bucket = self.__buckets[self.__get_bucket(key)]
            if bucket.empty:
                self.__full_buckets += 1
            bucket.append((key, value))

    



    def keys(self) -> Iterator[KT]:
        # iterator of keys within the hashmap
        for bucket in self.__buckets:
            for item in bucket:
                yield item[0]
    

    
    def values(self) -> Iterator[VT]:
        # iterator of the values within the hashmap
        for bucket in self.__buckets:
            for item in bucket:
                yield item[1]
    


    def items(self) -> Iterator[Tuple[KT, VT]]:
        # iterator of the items (key-value pairs I think) in hashmap
        for bucket in self.__buckets:
            for item in bucket:
                yield item
    
            
    def __delitem__(self, key: KT) -> None:
        bucket = self.__buckets[self.__get_bucket(key)]
        bucket.remove(self.__find_key_val_pair(key))
        if bucket.empty:
            self.__full_buckets-= 1


    
    def __contains__(self, key: KT) -> bool:
        try:
            self.__find_key_val_pair(key)
            return True
        except KeyError:
            return False
    


    def __len__(self) -> int:
        sum = 0
        
        for b in self.__buckets:
            sum += len(b)
        
        return sum
    


    def __iter__(self) -> Iterator[KT]:
        return self.keys()
    

    
    def __eq__(self, other: object) -> bool:
        # compare num items
        if len(self) != len(other):
            return False
        
        # compare iteration over values in buckets
        for i in range(self.__num_buckets):
            for j in range(len(self.__num_buckets[i])):
                if not self.__num_buckets[i][j] in other:
                    return False
        
        return True
                    
            

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)