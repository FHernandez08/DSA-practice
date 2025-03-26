def binary_iterative(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 9

# print(binary_iterative(arr=array, target=target_value))
def binary_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_recursive(arr, target, mid + 1, high)
    else:
        return binary_recursive(arr, target, low, mid - 1)


array_rec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_rec = 9

print(binary_recursive(arr=array_rec, target=target_rec, low=0, high=len(array_rec) - 1))
    