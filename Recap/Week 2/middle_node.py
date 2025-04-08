# Find Middle Node of a Linked List
# Given the head of a singly linked list, find and return the middle node. If there are two middle nodes, return the second one.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        

def find_middle(head):
    if head is None:
        return None
    
    if head.next is None:
        return head
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(find_middle(head).value)  # Expected: ListNode(3)