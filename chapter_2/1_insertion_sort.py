"""
Insertion Sort

Remember Insertion sort is like managing cards in a game. compare with each one and inser it in a proper location

psuedocode
1. start with second element in the array.
2. look backwards and compare & exchange
3. keep doing it for each element in the array

i = 1 to n
j = i-1 to 0 (backwards)


"""


def insertion_sort(array):
    for j in range(1, len(array)):
        val = array[j]
        i = j - 1
        while i >= 0 and array[i] > val:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = val
    return array


def insertion_sort_descending(array):
    for j in range(1, len(array)):
        val = array[j]
        i = j - 1
        while i >= 0 and array[i] < val:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = val
    return array


if __name__ == "__main__":
    print insertion_sort([5, 2, 4, 6, 1, 3])
    print insertion_sort_descending([5, 2, 4, 6, 1, 3])