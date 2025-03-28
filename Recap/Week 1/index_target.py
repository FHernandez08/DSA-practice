def index_binary(arr, target):
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


# test case
array_1 = [1, 2, 4, 6, 8, 10, 12]
target = 6
print(index_binary(arr=array_1, target=target))