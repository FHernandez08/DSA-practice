def binary_recursive(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_recursive(arr, mid + 1, high, target)
        else:
            return binary_recursive(arr, low, mid - 1, target)
    else:
        return -1
    
array_test = [1, 4, 6, 9, 11, 14, 16, 20, 25, 34, 43, 56, 65, 72]
x = 44

result = binary_recursive(array_test, 0, len(array_test) - 1, x)

if result != -1:
    print("The index to find x is:", result)
else:
    print("The item does NOT appear in the array!")