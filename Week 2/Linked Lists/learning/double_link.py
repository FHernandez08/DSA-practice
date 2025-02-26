class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    # returns the value of the current node    
    def get_value(self):
        return self.value
    
    # returns the previous address of the current node
    def get_prev_node(self):
        return self.prev
    
    # returns the next address of the current node
    def get_next_node(self):
        return self.next
    
    # sets the next node (removing the current node)
    def set_next_node(self, next):
        self.next = next
        
    # sets the prev node (removing the current node)
    def set_prev_node(self, prev):
        self.prev = prev
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # adds node to the head of the list
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head
        
        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
            
        self.head = new_head
        
        if self.tail == None:
            self.tail = new_head
    
    # adds node to the tail of the list
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail
        
        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
            
        self.tail = new_tail
        
        if self.head == None:
            self.head = new_tail

    # removes node from the head
    def remove_head(self):
        removed_head = self.head
        
        if removed_head == None:
            return None
        
        self.head = removed_head.get_next_node()
        
        if self.head != None:
            self.head.set_prev_node(None)
        
        if removed_head == self.tail:
            self.remove_tail()
        
        return removed_head.get_value()
    
    # removes node from the tail
    def remove_tail(self):
        removed_tail = self.tail
        
        if removed_tail == None:
            return None
        
        self.tail = removed_tail.get_prev_node()
        
        if self.tail != None:
            self.tail.set_next_node(None)
        
        if self.tail == self.head:
            self.remove_head()
            
        return removed_tail.get_value()
    
    # finds node's specific location by its value and removes it
    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        curr_node = self.head
        
        while curr_node != None:
            if curr_node.get_value() == value_to_remove:
                node_to_remove = curr_node
                break
            
            curr_node = curr_node.get_next_node()
            
        if node_to_remove == None:
            return None