"""
2.3-7
Describe a O(n lg n) time algorithm that, given a set S of n integers and another integer x, determines whether or not there exist two elements in S whose sum is exactly x.
"""

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

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def mergesort(A, p, r):
    if p < r:
        q = (p + (r - 1)) // 2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)
    return A


def bin_search(arr, l, r, x):
    if l < r:
        mid = (l + (r - 1)) / 2
        if arr[mid] == x:
            return True
        if arr[mid] > x:
            return bin_search(arr, l, mid-1, x)
        return bin_search(arr, mid+1, r, x)
    return False


def bin_search_1(arr, l, r, x):
    if l < r:
        mid = (l + (r - 1)) / 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return bin_search_1(arr, l, mid-1, x)
        return bin_search_1(arr, mid+1, r, x)
    return -1


def pair_exists(s, x):
    """
    1. sort using merge sort O(nlogn)
    2. search compliment using binary search O(logn)
    total = O(nlogn) + O(logn) == 0(logn)
    """
    if not s:
        return False
    l = len(s)
    s = mergesort(s, 0, l - 1)  # takes O(nlogn)
    for i in range(l):
        # problem will exist for values like 8 and ith value s again 8
        if bin_search(s, 0, l - 1, x - s[i]):
            return True
    return False


def pair_exists_1(s, x):
    """
    1. sort using merge sort
    2. use two pointer method to see if the pair has sum and stop whereever the sum is < x
    """
    if not s:
        return False
    n = len(s)
    s = mergesort(s, 0, n - 1)  # takes O(nlogn)
    l = 0
    r = n-1
    while l <= r:
        if s[l] + s[r] == x:
            return True
        elif s[l] + s[r] > x:
            r -= 1
        else:
            l += 1
    return False


def pair_exists_2(s, x):
    """
    1. sort using merge sort O(nlogn)
    2. search compliment using binary search O(logn)
    total = O(nlogn) + O(logn) == 0(logn)
    """
    if not s:
        return False
    l = len(s)
    s = mergesort(s, 0, l - 1)  # takes O(nlogn)
    for i in range(l):
        # problem will exist for values like 8 and ith value s again 8
        search_val = bin_search_1(s, 0, l - 1, x - s[i])
        if search_val != -1 and search_val != i:
            return True
    return False



print pair_exists([3, 4, 6, 2, 7], 9)
print pair_exists([3, 4, 6, 2, 7], 15)
print pair_exists_1([3, 4, 6, 2, 7], 9)
print pair_exists_1([3, 4, 6, 2, 7], 15)
print pair_exists_2([3, 4, 6, 2, 7], 9)
print pair_exists_2([3, 4, 4, 2, 7], 8)
print pair_exists_2([3, 4, 6, 2, 7], 15)
