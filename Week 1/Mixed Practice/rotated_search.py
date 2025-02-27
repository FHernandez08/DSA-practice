# Search in Rotated Sorted Array (Binary Search)
# Given a rotated sorted array (nums) of distinct integers and an integer (target). Implement a function to return the index of target
# if found, otherwise return -1. Must run in O (log n) time complexity.

def sorted_array(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target < nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(sorted_array(nums, target))