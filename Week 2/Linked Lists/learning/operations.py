# Initializing a node
class Node:
    def __init__(self, data):
        self.data = data  # Assigns the given data to the node
        self.next = None  # Initialize the next attribute to null
        
# Creating a linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        
        # Insert node at the beginning
        def insertAtBeginning(self, new_data):
            new_node = Node(new_data)  # Create a new node 
            new_node.next = self.head  # Next for new node becomes the   current head
            self.head = new_node  # Head now points to the new node
            
        # Insert a new node at the end of the list
        def insertAtEnd(self, new_data):
            new_node = Node(new_data)  # Create a new node
            if self.head is None:
                self.head = new_node  # If the list is empty, make the new node the head
                return
            last = self.head 
            while last.next:  # Otherwise, traverse the list to find the last node
                last = last.next
            last.next = new_node  # Make the new node the next node of the last node
        
        # Delete a node from the beginning of list
        def deleteFromBeginning(self):
            if self.head is None:
                return "The list is empty" # If the list is empty, return this string
            self.head = self.head.next  # Otherwise, remove the head by making the next node the new head
            
        # Delete node from the end
        def deleteFromEnd(self):
            if self.head is None:
                return "The list is empty" 
            if self.head.next is None:
                self.head = None  # If there's only one node, remove the head by making it None
                return
            temp = self.head
            while temp.next.next:  # Otherwise, go to the second-last node
                temp = temp.next
            temp.next = None  # Remove the last node by setting the next pointer of the second-last node to None
            
        # Search the value in linked list
        def search(self, value):
            current = self.head  # Start with the head of the list
            position = 0  # Counter to keep track of the position
            while current: # Traverse the list
                if current.data == value: # Compare the list's data to the search value
                    return f"Value '{value}' found at position {position}" # Print the value if a match is found
                current = current.next
                position += 1
            return f"Value '{value}' not found in the list" 