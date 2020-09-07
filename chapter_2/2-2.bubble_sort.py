"""
Bubble sort

Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order.
BUBBLESORT(A)
1 for i = 1to A.length-11
2     for j =A.length down to i
3.      if A[j] < A[j-1]
            # swap elements

Worst Case: O(n**2)
Best Case: O(n)
Average Case: O(n ** 2)
"""


def bubblesort(array):
    val = 1
    for i in range(len(array)):
        for j in range(0, len(array) - val):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        val += 1
    return array

print bubblesort([5, 4, 3, 2, 1])
