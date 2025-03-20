def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
            

nums = [2, 3, 4, 6, 7, 9, 10, 11, 14]
target = 11

print(binary_search(nums, target))