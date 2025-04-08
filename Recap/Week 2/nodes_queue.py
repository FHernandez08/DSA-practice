# Count Tree Nodes Using a Queue
# Given the root of a binary tree, use a queue to count how many nodes are in the tree. Return the total count.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def count_nodes(root):
    queue = deque()
    count = 0
    
    if root is None:
        return 0
    
    queue.append(root)
    while queue:
        current = queue.popleft()
        count += 1
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
            
    return count


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(count_nodes(root))  # Expected: 5