def merge_modificado(A,B):
    i=j=0
    C = []
    while i < len(A):
        for k in range(len(B)):
            if A[i] <= B[k]:
                C.append([A[i], B[k]])
                print('Pareja: ', A[i], B[k])
        i+=1
    i=j=0
    while i < len(A):
        if len(A) == 1:
            break
        else:
            A_copy = A[i+1:]
            for k in range(len(A_copy)):
                if A[i] <= A_copy[k]:
                    C.append([A[i], A_copy[k]])
                    print('Pareja: ', A[i], A_copy[k])
        i+=1
    while j < len(B):
        if len(B) == 1:
            break
        else:
            B_copy = B[j+1:]
            for k in range(len(B_copy)):
                if B[j] <= B_copy[k]:
                    C.append([B[j], B_copy[k]])
                    print('Pareja: ', B[j], B_copy[k])
        j+=1
    return C
def sorted_pairs(A):
    length = len(A)
    array_1 = A[:length//2]
    array_2 = A[length//2:]
    C = merge_modificado(array_1,array_2)
    return array_1 , array_2, C
print(sorted_pairs([2,3,3]))
print(sorted_pairs([1,6,3,2]))
print(sorted_pairs([2,3,5,1,3]))

