class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
def merge_two_lists(list_1, list_2):
    # Need dummy to start the merged list
    dummy = ListNode(-1)
    curr = dummy
    
    while list_1 and list_2:
        if list_1.value <= list_2.value:
            curr.next = list_1
            list_1 = list_1.next
            
        else:
            curr.next = list_2
            list_2 = list_2.next
            
        curr = curr.next 
    
    if list_1:
        curr.next = list_1
    if list_2:
        curr.next = list_2
        
    
    return dummy.next

# list1: 1 -> 3 -> 5
# list2: 2 -> 4 -> 6

a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)

b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(6)