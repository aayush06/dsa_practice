"""
used to strore key value pair
uses a hash function to compute an index into an array in which an element will be inserted or searched.
collision resolution - 
    Separate chaining (open hashing)
        To store an element in the hash table you must insert it into a specific linked list. 
        If there is any collision (i.e. two different elements have same hash value) then store 
        both the elements in the same linked list.
    Linear Probing (open addressing or closed hashing)
        all entry records are stored in the array itself, 
        If the slot at the hashed index is unoccupied, then the entry record is inserted in slot 
        at the hashed index else it proceeds in some probe sequence until it finds an unoccupied slot.
        Data set must have unique elements.
    Quadratic Probing 
        when the slot at a hashed index for an entry record is already occupied, you must start traversing until you find an unoccupied slot.
        The interval between slots is computed by adding the successive value of an arbitrary polynomial in the original hashed index.
        Data set must have unique elements.
    Double hashing
        the interval between successive probes is computed by using two hash functions.
"""

class HashTable: 
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity
        
    def _hash(self, key): 
        return hash(key) % self.capacity
    
    def insert(self, key, value): 
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = value
            self.size += 1
        else:
            print("Collision occured")
            return 0
        
    def search(self, key):
        index = self._hash(key)
        return self.table[index]
    
    def remove(self, key):
        index = self._hash(key)
        self.table[index] = None
        
ht = HashTable(5)
ht.insert("apple", 3) 
ht.insert("banana", 2) 
value = ht.search("apple")
print(value)
ht.remove("apple")
value = ht.search("apple")
print(value)
