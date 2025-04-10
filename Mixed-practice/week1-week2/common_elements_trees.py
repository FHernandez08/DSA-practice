# Given two binary trees, return a list of values that appear in both trees, and should NOT contain duplicates.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def collect_values(node, values_set):
    if node:
        values_set.add(node.value)
        collect_values(node.left, values_set)
        collect_values(node.right, values_set)
        
def similar_values(node, values_set, common_set):
    if node:
        if node.value in values_set:
            common_set.add(node.value)
        similar_values(node.left, values_set, common_set)
        similar_values(node.right, values_set, common_set)
        
def common_trees(tree1, tree2):
    values_tree1 = set()
    collect_values(tree1, values_set=values_tree1)
    
    common_values = set()
    similar_values(tree2, values_set=values_tree1, common_set=common_values)
    
    return list(common_values)


###### TEST CASE #1 ######
# Tree 1
t1 = TreeNode(5)
t1.left = TreeNode(1)
t1.right = TreeNode(8)
t1.right.left = TreeNode(3)

# Tree 2
t2 = TreeNode(3)
t2.left = TreeNode(5)
t2.right = TreeNode(7)
t2.left.left = TreeNode(1)

print(sorted(common_trees(t1, t2)))  # Output: [1, 3, 5]

###### TEST CASE #2 ######
# Tree 1
t1 = TreeNode(10)
t1.left = TreeNode(20)
t1.right = TreeNode(30)

# Tree 2
t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)

print(common_trees(t1, t2))  # Output: []