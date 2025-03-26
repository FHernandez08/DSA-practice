# Check for duplicates in an array
def check_duplicates(arr):
    duplicates = []
    non_duplicates = set()
    
    for item in arr:
        if item in non_duplicates:
            duplicates.append(item)
            return True
        else:
            non_duplicates.add(item)
    
    return False
        

array = [1, 2, 3, 4, 4, 6, 7, 8]
print(check_duplicates(arr=array))