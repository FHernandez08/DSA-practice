dict_array = [1, 4, 5, 1, 5, 2, 8, 7, 5, 1, 3, 7, 9, 0, 3, 5]

def frequency(arr):
    duplicates = []
    non_duplicates = {}
    
    for item in dict_array:
        if item in non_duplicates:
            duplicates.append(item)
        else:
            non_duplicates[item] = True
            
    print(non_duplicates)
    print(duplicates)
    
frequency(dict_array)