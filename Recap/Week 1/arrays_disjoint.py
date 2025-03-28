def disjoint_arrays(arr1, arr2):
    if len(arr1) != 0 and len(arr2) != 0:
        return True
    return False

# Test Case 1
array_1 = [1, 2, 3, 4]
array_2 = [5, 6, 7, 8]
# print(disjoint_arrays(arr1=array_1, arr2=array_2))

# Test Case 2
array_3 = []
array_4 = []
# print(disjoint_arrays(arr1=array_3, arr2=array_4))