# Unique pairs with target sum (Hashing & Sets)
# Given an integer array (nums) and an integer (target), return the number of unique pairs (a, b) such that a + b == target.
# A pair is considered unique if the same two numbers are not counted twice in a different order.

def unique_pair_sum(arr, target):
    seen = set()
    unique_pairs = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            unique_pairs.add(pair)
        seen.add(num)
    
    return len(unique_pairs)

nums = [1, 3, 2, 2, 4, 5, 3]
target = 5

print(unique_pair_sum(nums, target))
    
    