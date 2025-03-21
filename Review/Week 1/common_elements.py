def common_elements(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    if (set_1.intersection(set_2)):
        return True
    return False

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [3, 4, 5, 6, 7, 8]

print(common_elements(list_1, list_2))