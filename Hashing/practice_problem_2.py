# Check for duplicates in an array

array = [1, 4, 5, 2, 6, 1, 7, 3, 4, 2, 6, 2, 1, 1, 3, 2]

def check_duplicates(arr):
    duplicates = []
    non_duplicates = {}
    
    for element in arr:
        if element in non_duplicates:
            duplicates.append(element)
        else:
            non_duplicates[element] = True