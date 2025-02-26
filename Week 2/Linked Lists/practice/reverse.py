class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverseLinkedList(head):
    temp = head
    prev = None

    while temp is not None:
        # stores the next node in the front variable - from head
        front = temp.next

        # reverses the pointer from the node to the previous node
        temp.next = prev

        # moves prev to current node for next iteration and creates the link with current and previous node
        prev = temp

        # advances traversal
        temp = front

    return prev


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.value, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverseLinkedList(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)