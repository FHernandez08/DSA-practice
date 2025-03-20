def search_insert(nums, target):
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
            
    if low > high:
        return low
    
    
nums = [2, 3, 4, 6, 7, 9, 10, 11, 14]
print(search_insert(nums, 11))  # Output: 7 (Found at index 7)
print(search_insert(nums, 8))   # Output: 5 (Would be inserted at index 5)