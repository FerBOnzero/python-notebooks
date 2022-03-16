#algorithm that returns an ordered array of three sorted arrays
def merge_arrays(array1, array2): 
    array3 = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            if array1[i] in array3:
                i += 1
            else: 
                array3.append(array1[i])
                i += 1
        else:
            if array2[i] in array3:
                j += 1
            else:
                array3.append(array2[j])
                j += 1
    while i < len(array1):
        if array1[i] in array3:
            i += 1
        else:
            array3.append(array1[i])
            i += 1
    while j < len(array2):
        if array2[j] in array3:
            j += 1
        else:
            array3.append(array2[j])
            j += 1
    return array3
    
def ordered_array(array1, array2, array3):
    return merge_arrays(merge_arrays(array1, array2), array3)
print(ordered_array([1,2,3,4,5], [1,2,3,4,5,6], [1,2,3,4,5,6]))
#therefore the complexity of this algorithm is O(n)