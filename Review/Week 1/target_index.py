def target_index(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


array = [1, 4, 5, 7, 8, 9, 11, 14]
target = 9

print(target_index(array, target))