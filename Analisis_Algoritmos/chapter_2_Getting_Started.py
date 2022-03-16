#insertion sort, complexity O(n^2)
def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1 
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
print('insertion sort: ', insertion_sort([5,2,4,6,1,3]))

#searching problem, complexity O(n)
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
print('linear search: ', linear_search([5,2,4,6,1,3], 2))

#merge, complexity O(n)
def merge(array1, array2):
    array3 = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    while i < len(array1):
        array3.append(array1[i])
        i += 1
    while j < len(array2):
        array3.append(array2[j])
        j += 1
    return array3
print('merge: ' ,merge([5,2,4,6,1,3], [1,2,3,4,5,6]))

#merge sort, complexity O(n log n)
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    array1 = merge_sort(array[:mid])
    array2 = merge_sort(array[mid:])
    return merge(array1, array2)
print('merge sort: ', merge_sort([5,2,4,6,1,3]))

#bubble sort, complexity O(n^2)
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array
print('bubble sort:', bubble_sort([5,2,4,6,1,3]))

#quick sort, complexity O(n log n)
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    array1 = []
    array2 = []
    for i in range(1, len(array)):
        if array[i] < pivot:
            array1.append(array[i])
        else:
            array2.append(array[i])
    return quick_sort(array1) + [pivot] + quick_sort(array2)
print('quick sort:', quick_sort([5,2,4,6,1,3]))

#counting sort, complexity O(n+k)
def counting_sort(array, k): #n is the length of the array, k is the range of the array
    count = [0] * k
    for i in range(len(array)):
        count[array[i]] += 1
    i = 0
    for j in range(k):
        while count[j] > 0:
            array[i] = j
            i += 1
            count[j] -= 1
    return array
print('counting sort:', counting_sort([5,2,4,6,1,3], 7))

#linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#list search on linked list
def linked_list_search(head, target):
    while head != None:
        if head.data == target:
            return True
        head = head.next
    return False

#even or odd number
def even_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
print('even or odd: ', even_odd(12))



