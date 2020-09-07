"""
2-4 Inversions
Let A[1 .. n]  be an array of n distinct numbers. If i < j and A[i]  > A[j] , then the pair (i, j)  is called an inversion of A.

a. List the five inversions of the array [2,3,8,6,1]
b. What array with elements from the set {1, 2 ... n } has the most inversions? How many does it have? - reverse order

array = [n, n-1, ... , 2, 1]
values
1. (2, 1)
2. (3, 2)
3. (3, 1)
4. (4, 3)
5. (4, 2)
6. (4, 1) and so on 
and if you look there will be 1, 2, 3, 4,  ... n-1 inversions ie n(n-1)/2 inversions will be present

c. What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer.
d. Give an algorithm that determines the number of inversions in any permutation on n elements in O(n lg n) worst-case time. (Hint: Modify merge sort.)
"""


def find_inversions(array):
    l = len(array)
    inversions = []
    for j in range(l):
        for i in range(j):
            if array[i] > array[j]:
                inversions.append((i, j))
            if len(inversions) == 5:
                break
    return inversions


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    i, j = 0, 0
    k = p
    inversions = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inversions = inversions + n1 -i + 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1
    return inversions


def mergesort(A, p, r):
    inversions = 0
    if p < r:
        q = (p + (r - 1)) // 2
        left = mergesort(A, p, q)
        right = mergesort(A, q + 1, r)
        inversions = merge(A, p, q, r) + left + right
    return inversions


def find_no_of_inversions_using_merge_sort(array):
    return mergesort(array, 0, len(array) - 1)


print find_inversions([2, 3, 8, 6, 1])
print find_no_of_inversions_using_merge_sort([2, 3, 8, 6, 1])
