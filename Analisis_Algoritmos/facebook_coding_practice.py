'''
You are given an array arr of N integers. For each index i, you are required to determine the 
number of contiguous subarrays that fulfill the following conditions:
    - The value at index i must be the maximum element in the contiguous subarrays, and
    - These contiguous subarrays must either start from or end on index i.
'''

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
  return list_sublist
print(count_subarrays([3, 4, 1, 6, 2]))   

#I think that the complexity of the code is O(n^2) :) 

'''
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if 
one pair includes at least one array index which the other doesn't, even if they include the same values.
'''
# [1,2,3], 5    ->  
def numberOfWays(arr, k):
  # Write your code here
  count = 0
  for i in range(len(arr)):
    value = arr[i]
    array = arr.copy()
    array.pop(i)
    for j in range(len(array)):
      if value + array[j] == k:        
        count += 1
  return int(count/2)
print(numberOfWays([1,2,3], 5))
arr = [1, 2, 3, 4, 3]
print(numberOfWays(arr, 6))
arr_2 =  [1, 5, 3, 3, 3]
print(numberOfWays(arr_2, 6))
# complexity of the code is O(n^2) :)

'''
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means 
replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
'''

def rotationalCipher(input, rotation_factor):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  list_alphabet_lower = list(alphabet)
  list_alphabet_upper = list(alphabet.upper())
  numbers = "0123456789"
  list_numbers = list(numbers)
  list_input = list(input)
  string_test = ''
  for i in range(len(list_input)):
    if list_input[i] in list_alphabet_lower:
      index_lower = list_alphabet_lower.index(list_input[i]) + rotation_factor
      while index_lower >= len(list_alphabet_lower):
          index_lower -= len(list_alphabet_lower)      
      list_input[i] = list_alphabet_lower[index_lower]
    elif list_input[i] in list_alphabet_upper:
      index_upper = list_alphabet_upper.index(list_input[i]) + rotation_factor
      while index_upper >= len(list_alphabet_upper):
        index_upper -= len(list_alphabet_upper) 
      list_input[i] = list_alphabet_upper[index_upper]
    elif list_input[i] in list_numbers:
      index_number = list_numbers.index(list_input[i]) + rotation_factor
      while index_number >= len(list_numbers):
        index_number -= len(list_numbers) 
      list_input[i] = list_numbers[index_number] 
    else:
      continue 
  for i in list_input:
    string_test += i
  return string_test
print(rotationalCipher("All-convoYs-9-be:Alert1", 4))
print(rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789", 39))
print(rotationalCipher('Zebra-493',3))
print(rotationalCipher('abcdZXYzxy-999.@', 200))
#complexity linear O(n) :)

'''
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive),
output[i] is equal to the product of the three largest elements out of arr[0..i] (or equal to -1 if i < 2, as arr[0..i] then includes fewer than three elements).
Note that the three largest elements used to form any product may have the same values as one another, but they must be at different indices in arr.
'''

def findMaxProduct(arr):
  # Write your code here
  empty_list = []
  if len(arr) < 2:
    empty_list = [-1]
    return empty_list
  elif len(arr) == 2:
    empty_list = [-1,-1]
    return empty_list
  else: 
    empty_list = [-1,-1]
    for i in range(2,len(arr)): 
      array_1 = arr.copy()
      value_1 = max(array_1[:i+1])
      array_1.pop(array_1.index(value_1)) 
      for j in range(len(array_1)):
        array_2 = array_1.copy()
        value_2 = max(array_2[:i])
        array_2.pop(array_2.index(value_2))
        for k in range(len(array_2)):
          array_3 = array_2.copy()
          value_3 = max(array_3[:i-1])
      empty_list.append(value_1 * value_2 * value_3)      
  return empty_list
print(findMaxProduct([2, 1, 2, 1, 2]))
print(findMaxProduct([1, 2, 3, 4, 5]))
# I think that the complexity is O(n^3) 

'''
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, 
the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that 
floor(x/2) pieces are now inside.
'''
def maxCandies(arr, k):
  # Write your code here
  array_test = []    
  while k > 0: 
    maximun = max(arr) 
    floor = maximun // 2
    array_test.append(maximun)
    arr.append(floor)
    arr.pop(arr.index(maximun))
    k -= 1 
  print(array_test)
  return  sum(array_test)
print(maxCandies([2, 1, 7, 4, 2],3))  
print(maxCandies([19, 78, 76, 72, 48, 8, 24, 74, 29], 3))
#I consider that the complexity of this algorithm is O(n) :) 

'''
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i]
is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
'''
def median(array):
  listSorted = sorted(array)
  if len(listSorted) % 2 == 1:
    indice = int((len(listSorted) - 1)//2)
    return int(listSorted[indice])  
  else:
    indice = int(len(listSorted)/2)
    median = sum(listSorted[indice -1 :indice +1])//2 
    return int(median)
print(median([5, 15, 1, 3]))

def findMedian(arr):
  # Write your code here
  count = 0
  empty_list = []
  array_medians = []
  while count < len(arr):
    count += 1
    empty_list.append(arr[:count])
  for i in empty_list:
    array_medians.append(median(i))
  return array_medians
print(findMedian([5, 15, 1, 3]))
print(findMedian([2, 4, 7, 1, 5, 3]))
#I consider that the complexity of findMedian(arr), is O(n)

'''
Matching Pairs
'''
def matching_pairs(s, t):
  # Write your code here
  empty_list = []
  empty_list.append(s)
  list_matching = []
  count_2 = 0

  for i in s:
    s_list = list(s)
    for j in s_list:
      empty_string = ''
      empty_string += s_list[s_list.index(j)]
      s_list[s_list.index(j)] = i 
      s_list[s_list.index(i)] = empty_string
      empty_list.append(''.join(s_list))
  list_matching = []
  count = 0
  empty_list = list(set(empty_list))
  for i in empty_list:
    for j in range(len(t)):
      if i[j] == t[j]:
        count += 1
        list_matching.append(i[j] + t[j])
  return (list_matching), empty_list 
print(matching_pairs("abcd", 'adcb'))
print(matching_pairs("mno", "mno"))

'''
Minimum Length Substrings
'''
def min_length_substring(s,t):
  empty_list = []
  empty_list.append(s)
  list_matching = []
  count_2 = 0

  for i in s:
    count = 0
    s_list = list(s)
    while count + 1 < len(s):
      list_matching.append(s[s.index(i):count + 1])
      count += 1
  list_matching = list(set(list_matching))
  for i in list_matching:
    count = 0
    for j in t:
      if j in list(i):
        count += 1
    if count == len(t):
      count_2 += 1
    else: 
      list_matching.pop(list_matching.index(i))
  return list_matching, count_2
print(min_length_substring('dcbefebce', 'fd'))





