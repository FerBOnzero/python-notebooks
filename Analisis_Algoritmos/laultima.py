def counting_pairs(A,B):
    answer = 0
    for i in range(len(A)):
        j = 0
        while j < len(B) and A[i] <= B[j]:
            print('Pareja: ', [A[i],B[j]])
            j += 1
        answer +=  j        
    return answer
def ordered_pairs(A):
    if len(A) == 1 or len(A) == 0:
        return 0
    else:
        mid = len(A)//2
        A1 = A[:mid]
        A2 = A[mid:]
        return ordered_pairs(A1) + ordered_pairs(A2) + counting_pairs(A1,A2)
print(ordered_pairs([2,3,3]))
print(ordered_pairs([1,6,3,2]))
print(ordered_pairs([1,4,5,7,8,9]))


