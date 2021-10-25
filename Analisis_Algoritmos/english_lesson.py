'''
You are given an array arr of N integers. For each index i, you are required to determine the 
number of contiguous subarrays that fulfill the following conditions:
    - The value at index i must be the maximum element in the contiguous subarrays, and
    - These contiguous subarrays must either start from or end on index i.
'''
# [1,3,2]   ->  2: [2], 1: [1], 3: [3], [2,3], [1,3]
def count_subarrays(arr):
  # Write your code here
  empty_dict = {}
  for i in arr:
    var_index = arr.index(i)
    index_new = var_index + 1
    empty_list = []
    count = 0
    maximun_left = max(arr[var_index:arr.index(i)+1])
    maximun_right = max(arr[var_index:index_new+count])
    while maximun_left == i:
      empty_list.append(arr[var_index:index_new])
      var_index -= 1
      if var_index < 0:
        break
      else:
        maximun_left = max(arr[var_index:index_new])
    var_index = arr.index(i)
    while maximun_right == i:
      empty_list.append(arr[var_index:index_new+count])
      count += 1
      if index_new + count > len(arr):
        break
      else:
        maximun_right = max(arr[var_index:index_new+count])
    empty_dict[i] = len(empty_list)
  list_sublist = list(empty_dict.values())
  for i in range(len(list_sublist)):
    list_sublist[i] -= 1
  return (list_sublist)
print(count_subarrays([1,3,2]))
