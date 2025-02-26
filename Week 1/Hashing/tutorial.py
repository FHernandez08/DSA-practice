# creates an item that will be added to the array
class Node: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None
  
  
class HashTable:
    # creates the hash table that will be added to and more
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.table = [None] * capacity 
        
    # hash function
    def _hash(self, key): 
        return hash(key) % self.capacity 
    
    # appends items to the array and also appends to the linked list at a certain index if
    # there's an existing value at that index
    def insert(self, key, value): 
        index = self._hash(key) 
        
        # appends node to the index of the hash table if there's nothing there
        if self.table[index] is None: 
            self.table[index] = Node(key, value) 
            self.size += 1
        
        # it chains the node to the existing node at the index
        else: 
            current = self.table[index] 
            while current: 
                if current.key == key: 
                    current.value = value 
                    return
                current = current.next
            new_node = Node(key, value) 
            new_node.next = self.table[index] 
            self.table[index] = new_node 
            self.size += 1
            
    # searches the node in the hash table by looking up the value and then comparing the keys,
    # if they match, return value
    # instead, move to the next one *current = current.next
    def search(self, key): 
        index = self._hash(key) 
  
        current = self.table[index] 
        while current: 
            if current.key == key: 
                return current.value 
            current = current.next
  
        raise KeyError(key) 
    
    # removes an item from the hash table by getting it's array, by removing the item
    # and reconnecting the linked list at the index of the hash table
    def remove(self, key): 
        index = self._hash(key) 
  
        previous = None
        current = self.table[index] 
  
        while current: 
            if current.key == key: 
                if previous: 
                    previous.next = current.next
                else: 
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current 
            current = current.next
  
        raise KeyError(key) 
    
    # returns the length of the hash table
    def __len__(self): 
        return self.size 


    # checks if the item is in the hash table -> callback function = search()
    def __contains__(self, key): 
        try: 
            self.search(key) 
            return True
        except KeyError: 
            return False