def binary_search(arr, low, high, target):
    if high >= low:
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        
        else:
            return binary_search(arr, mid + 1, high, target)
    
    else:
        return -1
    
arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")