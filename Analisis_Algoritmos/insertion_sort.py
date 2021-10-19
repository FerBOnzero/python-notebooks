#function that returns the sorted list
def insertion_sort(list):
    #for each element in the list
    for i in range(1, len(list)):
        #set the current element as the key
        key = list[i]
        #set the position of the current element
        j = i - 1
        #while the current element is less than the key and the position is greater than 0
        while j >= 0 and key < list[j]:
            #move the element to the right
            list[j+1] = list[j]
            #decrease the position
            j -= 1
        #set the current element to the key
        list[j + 1] = key
        print(list, 'miau')
    #return the sorted list
    return list
print(insertion_sort([5,2,4,6,1,3]))

def merge_sort(list):
    #if the list has only one element
    if len(list) <= 1:
        #return the list
        return list
    #set the middle of the list
    middle = len(list) // 2
    #set the left list
    left = list[:middle]
    #set the right list
    right = list[middle:]
    #set the left list to the merge sort of the left list
    left = merge_sort(left)
    #set the right list to the merge sort of the right list
    right = merge_sort(right)
    #set the sorted list
    sorted_list = []
    #while the left list and the right list are not empty
    while len(left) > 0 and len(right) > 0:
        #if the first element of the left list is less than the first element of the right list
        if left[0] < right[0]:
            #add the first element of the left list to the sorted list
            sorted_list.append(left.pop(0))
            print('left: ' ,left)
        #if the first element of the left list is greater than the first element of the right list
        else:
            #add the first element of the right list to the sorted list
            sorted_list.append(right.pop(0))
            print('right: ', right)
    #while the left list is not
    return sorted_list + left + right
print(merge_sort([9,8,7,3,2,1]))
print([9,7,8]+[1,2,3])
