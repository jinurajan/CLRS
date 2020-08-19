"""
Selection Sort

Select an element and find the smallest number in the array and swap. continue until we reach the end of the array

Worst Case O(N2)
Average Case O(N2)
Best Case O(N2)

"""


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] <= array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def selection_sort_descending(array):
    n = len(array)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if array[j] >= array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]

    return array



print selection_sort([6, 5, 4, 3, 2, 1])
print selection_sort_descending([1, 2, 3, 4, 5, 6])

