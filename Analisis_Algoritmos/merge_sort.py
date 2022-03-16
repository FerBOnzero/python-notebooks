def merge(A,B):
    C = []
    while A != [] and B != []:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    if A == []:
        C += B
    else:
        C += A
    return C
def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A)//2
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left,right)
print(merge_sort([1,3,5,7,9,2,4,6,8,0]))