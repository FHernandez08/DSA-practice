def sort_arr(arr):
    if len(arr) <= 1:
        return arr
    
    left, right = 0, len(arr) - 1
    
    mid = (left + right) // 2
    left_subarray = sort_arr(arr[:mid])
    right_subarray = sort_arr(arr[mid:])
    
    return merge(left_subarray, right_subarray)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
        
    return result   