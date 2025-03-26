def unique_elements(arr):
    duplicates = []
    unique_items = set()
    
    for item in arr:
        if item in unique_items:
            duplicates.append(item)
        unique_items.add(item)
        
    return unique_items


array = [1, 2, 3, 4, 4, 5, 6, 2, 2, 4, 1, 5, 6]

print(unique_elements(arr=array))