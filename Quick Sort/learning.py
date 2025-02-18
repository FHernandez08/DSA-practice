def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    smaller, equal, larger = [], [], []
    
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    return quick_sort(smaller) + equal + quick_sort(larger)

array = [24, 11, 14, 15, 43, 22, 5, 64, 43, 6, 2, 55]

sorted_array = quick_sort(array)

print(sorted_array)
