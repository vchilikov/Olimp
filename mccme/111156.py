def SelectionSort(A):
    newArr = []
    while len(A):
        max = 0
        for i in range(len(A)):
            if A[max] < A[i]:
                max = i
        newArr.append(A.pop(max))
    return newArr

A = list(map(int, input().split()))
print(" ".join(map(str, SelectionSort(A))))
