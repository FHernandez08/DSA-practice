# binary search w/ the variations

# basic binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)
print(f"Target {target} found at index: {result}")

# recursive binary search
def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
result = recursive_binary_search(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index: {result}")
    
# Finding the first occurrence
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 2
result = first_occurrence(arr, target)
print(f"First occurrence of {target} found at index: {result}")

# Finding the last occurrence
def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr = [1, 2, 2, 2, 3, 4, 4, 5]
target = 4
result = last_occurrence(arr, target)
print(f"Last occurrence of {target} found at index: {result}")

# Finding the floor and ceiling
def floor(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            result = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def ceiling(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            result = arr[mid]
            right = mid - 1
    
    return result

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 6
floor_result = floor(arr, target)
ceiling_result = ceiling(arr, target)
print(f"Floor of {target}: {floor_result}")
print(f"Ceiling of {target}: {ceiling_result}")

# Search in Rotated Sorted Array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = search_rotated(arr, target)
print(f"Target {target} found at index: {result}")