def merge_without_order(array1, array2):
    array3 = []
    i = 0
    while i < len(array1):
        if array1[i] in array2:
            array2.remove(array1[i])
            array3.append(array1[i])
        else:
            array3.append(array1[i])
        i += 1
    for j in array2:
        array3.append(j)
    return array3      

def merge_nosort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    array1 = merge_nosort(array[:mid])
    array2 = merge_nosort(array[mid:])
    return merge_without_order(array1, array2)
print('merge no sort: ', merge_nosort([5,2,1,4,6,1,3]))
print('merge no sort: ', merge_nosort([3,5,2,1,3,5,4,6,1]))
print('merge no sort: ', merge_nosort([1,2,3,4,5,6,7,8,9,10]))
print('merge no sort: ', merge_nosort([2,1,2,1,2,1,3]))

