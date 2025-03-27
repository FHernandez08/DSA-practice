def kth_largest(arr, k):
    if len(arr) == 1 and k == 1:
        return arr[0]
    
    sorted_array = merge_sort(arr)
    
    return sorted_array[len(arr) - k]
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    return merge(sorted_left, sorted_right)

def merge(left, right):
    i, j = 0, 0
    merged_array = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
    
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    
    return merged_array

###### TEST CASES ######
# 1. Normal Case
arr = [7, 1, 3, 5, 9, 2]
k = 3
# The sorted array is [1, 2, 3, 5, 7, 9]
# The 3rd largest element is 5
print(kth_largest(arr, k))  # Expected output: 5

# 2. Small Array
arr = [3, 1]
k = 1
# The sorted array is [1, 3]
# The 1st largest element is 3
print(kth_largest(arr, k))  # Expected output: 3

# 3. Array with Repeated Elements
arr = [5, 1, 5, 3, 5]
k = 2
# The sorted array is [1, 3, 5, 5, 5]
# The 2nd largest element is 5
print(kth_largest(arr, k))  # Expected output: 5

# 4. k is 1 (Largest Element)
arr = [10, 20, 30, 40, 50]
k = 1
# The sorted array is [10, 20, 30, 40, 50]
# The 1st largest element is 50
print(kth_largest(arr, k))  # Expected output: 50

# 5. k equals length of the array (Smallest Element)
arr = [10, 20, 30, 40, 50]
k = 5
# The sorted array is [10, 20, 30, 40, 50]
# The 5th largest element is 10
print(kth_largest(arr, k))  # Expected output: 10

# 6. Edge Case with Single Element
arr = [99]
k = 1
# The sorted array is [99]
# The 1st largest element is 99
print(kth_largest(arr, k))  # Expected output: 99