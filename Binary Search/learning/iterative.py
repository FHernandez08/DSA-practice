def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

numbers = [3, 6, 7, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]

target = 31

result = binary_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")