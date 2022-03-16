#function that return an ordered pairs complexity O(nlogn)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append([left[i], right[j]])
            j += 1
    return result
def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)
print(merge_sort([2,3,3]))
print(merge_sort([1,6,3,2]))

def numIdenticalPairs(nums) -> int:
    countPairs = 0
    counter = {}
    for n in nums:
        if n in counter:
            countPairs += counter[n]
            counter[n] += 1    
        else:
            counter[n] = 1
    return countPairs

print(numIdenticalPairs([2,3,3]))


def ordered_pairs(lst): 
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        left = ordered_pairs(lst[:mid])
        right = ordered_pairs(lst[mid:])
        return merge(left, right)
print(ordered_pairs([2,3,3]))

# Merge two sorted sublists `A[low … mid]` and `A[mid+1 … high]`
def merge(A, B, middle, length):
    aux = A.copy()
    k = i = 0
    j =  middle + 1
    inversionCount = 0
 
    # while there are elements in the left and right runs
    while i <= middle and j <= length:
        if A[i] <= A[j]:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (middle - i + 1)
            
        else:
            aux[k] = A[i]
            i = i + 1        # NOTE
 
        k = k + 1
 
    # copy remaining elements
    while i <= middle:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
 
    ''' no need to copy the second half (since the remaining items
        are already in their correct position in the temporary array) '''
 
    # copy back to the original list to reflect sorted order
    for i in range(length+1):
        A[i] = aux[i]
 
    return inversionCount
 
 
# Sort list `A[low…high]` using auxiliary list `aux`
def mergesort(A):
    aux = A.copy()
    # base case
    if len(A) <= 1:        # if run size <= 1
        return 0
 
    # find midpoint
    middle = len(A) // 2
    inversionCount = 0
 
    # recursively split runs into two halves until run size <= 1,
    # then merges them and return up the call chain
 
    inversionCount += mergesort(A[:middle])       # split/merge left half
    inversionCount += mergesort(A[middle:])  # split/merge right half
    inversionCount += merge(A[:middle], A[middle:], middle ,len(A))     # merge the two half runs
 
    return inversionCount
 
 
if __name__ == '__main__':
 
    A = [2,3,5,1,3]
    aux = A.copy()
 
    # get the inversion count by performing merge sort on a list
    print("Inversion count is", mergesort(A))

    # Python 3 program to count inversions in an array


# Function to Use Inversion Count
def mergeSort(arr, n):
	# A temp_arr is created to store
	# sorted array in merge function
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions

def _mergeSort(arr, temp_arr, left, right):

	# A variable inv_count is used to store
	# inversion counts in each recursive call

	inv_count = 0

	# We will make a recursive call if and only if
	# we have more than one elements

	if left < right:

		# mid is calculated to divide the array into two subarrays
		# Floor division is must in case of python

		mid = (left + right)//2

		# It will calculate inversion
		# counts in the left subarray

		inv_count += _mergeSort(arr, temp_arr,
									left, mid)

		# It will calculate inversion
		# counts in right subarray

		inv_count += _mergeSort(arr, temp_arr,
								mid + 1, right)

		# It will merge two subarrays in
		# a sorted subarray

		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count

# This function will merge two subarrays
# in a single sorted subarray
def merge(arr, temp_arr, left, mid, right):
	i = left	 # Starting index of left subarray
	j = mid + 1 # Starting index of right subarray
	k = left	 # Starting index of to be sorted subarray
	inv_count = 0

	# Conditions are checked to make sure that
	# i and j don't exceed their
	# subarray limits.

	while i <= mid and j <= right:

		# There will be no inversion if arr[i] <= arr[j]

		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			# Inversion will occur.
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	# Copy the remaining elements of left
	# subarray into temporary array
	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	# Copy the remaining elements of right
	# subarray into temporary array
	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	# Copy the sorted subarray into Original array
	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]
		
	return inv_count

# Driver Code
# Given array is
arr = [2,3,5,1,3]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)

# This code is contributed by ankush_953




def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count   
def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2 
    left = merge_count_inversion(lst[:middle])
    right = merge_count_inversion(lst[middle:])
    result = merge_count_split_inversion(left, right)
    return result
def count_inversion(lst):
    return merge_count_inversion(lst)
print(count_inversion([2,3,3]))


#test code
input_array_1 = []  #0
input_array_2 = [1] #0
input_array_3 = [1, 5]  #0
input_array_4 = [4, 1] #1
input_array_5 = [4, 1, 2, 3, 9] #3
input_array_6 = [4, 1, 3, 2, 9, 5]  #5
input_array_7 = [4, 1, 3, 2, 9, 1]  #8

print(count_inversion(input_array_7))
print count_inversion(input_array_2)
print count_inversion(input_array_3)
print count_inversion(input_array_4)
print count_inversion(input_array_5)
print count_inversion(input_array_6))
print(count_inversion(input_array_7))