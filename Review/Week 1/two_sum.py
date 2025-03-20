def two_sum(nums, target):
    hash_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[i] = num
            
    return []


nums = [2, 3, 4, 5, 7, 8, 10, 15]
target = 12

print(two_sum(nums, target))