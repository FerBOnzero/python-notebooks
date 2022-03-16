
def merge_and_count(A,B):
    count = 0
    #C = []
    i = j = 0
    while i < len(A) or j < len(B):
        if j > len(B) - 1 or (i < len(A) and A[i] > B[j]):
     #       C.append(A[i])
            i += 1
            count = count + j
        else:
      #      C.append(B[j])
            j += 1

    return count
def sort_and_count(A):
    if len(A) <= 1:
        return A, 0
    else:
        mid = len(A)//2
        A1 = A[:mid]
        A2 = A[mid:]
        A1.sort()
        A2.sort()
        count1 = sort_and_count(A1)
        count2 = sort_and_count(A2)
        count3 = merge_and_count(A1,A2)
        
        return (count3) + (count1) + (count2)
print(sort_and_count([2,3,3]))
print(sort_and_count([1,6,3,2]))
print(sort_and_count([1,4,5,7,8,9]))
print(sort_and_count([2,3,4,8,1,2]))