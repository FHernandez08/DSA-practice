class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    # gets the value of node
    def get_value(self):
        return self.value
    
    # returns the value of the next node
    def get_next_node(self):
        return self.next
    
    # creates the link and points to the next node of the current node
    def set_next_node(self, next):
        self.next = next
        
        
class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        
    # return the head of the linked list
    def get_head_node(self):
        return self.head
    
    # inserts the node at the beginning of the list
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head)
        self.head = new_node
    
    # creates a list from the linked list
    def string_list(self):
        string_list = ""
        current_node = self.get_head_node()
        
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            
            current_node = current_node.get_next_node()
        
        return string_list
    
    # removes the node from either the start/location/end
    def remove_node(self, value_remove):
        current_node = self.get_head_node()
        
        # start of the linked list = head
        if current_node.get_value() == value_remove:
            self.head = current_node.get_next_node()
        
        # any other place in the linked list
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = Node
                else:
                    current_node = next_node