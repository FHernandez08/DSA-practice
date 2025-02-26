def quick_sort(arr):
    if len(arr) < 1:
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

array = [12, 31, 35, 22, 44, 23, 55, 67, 87, 66, 2]
test = quick_sort(array)

print(test)