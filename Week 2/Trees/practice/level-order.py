from collections import deque

class Node:
    def __init__(self, data=None):
        self.value = data
        self.left = None
        self.right = None
        
class level_traversal:
    def __init__(self, root_value):
        self.root = Node(root_value)
        
    def level_order_traversal(self):
        if not self.root:
            return
        
        queue = deque()
        queue.append(self.root)
    
        while queue:
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                print(node.value, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            
#### TEST ####
# tree = level_traversal(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.level_order_traversal()

#### TEST 2 ####
# Example to test the level-order traversal
tree = level_traversal(1)  # Create the tree with root value 1
tree.root.left = Node(2)  # Left child of root
tree.root.right = Node(3)  # Right child of root
tree.root.left.left = Node(4)  # Left child of node 2
tree.root.left.right = Node(5)  # Right child of node 2
tree.root.right.left = Node(6)  # Left child of node 3
tree.root.right.right = Node(7)  # Right child of node 3

# Perform level-order traversal
tree.level_order_traversal()