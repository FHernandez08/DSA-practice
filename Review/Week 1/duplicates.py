def contain_duplicates(nums):
    non_duplicates = set()
    duplicates = []
    
    for num in nums:
        if num in duplicates:
            return True
        else:
            non_duplicates.add(num)
            duplicates.append(num)
    return False
            
            
list_nums = [1, 2, 2, 3, 4, 5, 6, 7]
print(contain_duplicates(list_nums))