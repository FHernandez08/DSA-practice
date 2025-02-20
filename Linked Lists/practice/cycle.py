class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def has_cycle(head):
    if not head:
        return False
    
    fast = head
    slow = head

    while fast is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True
    
    return False