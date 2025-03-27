def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    # where the array is divided in the middle
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    return merge(left_arr, right_arr)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.right(right[j])
            j += 1
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

array = [1, 5, 4, 6, 10, 14, 11, 9]
sorted_array = merge_sort(array)
print(sorted_array)