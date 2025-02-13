curr_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

new_list = list(curr_set)
updated_list = []

for item in new_list:
    if item % 2 == 0:
        updated_list.append(item)
        
    new_set = set(updated_list)

print(new_set)