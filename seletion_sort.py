def selection_sort(list):
    """An unstable sorting function that finds the min of a list and swaps it with the element
        at the kth iteration.
       Input: Unsorted list of size N integers
       Output: sorted list of size N integers
       Time Complexity: O(N)
       Space Complexity: O(1)
    """
    for i in range(len(list)):
        minimum = min(list[i:])
        if minimum < list[i]:
            temp = list[minimum + i]
            list[minimum + i] = list[i]
            list[i] = temp
    return list


def min(list):
    """A function that finds the minimum of a list
    Input: Unsorted list of integers of size n
    Output: The index of the smallest element

    """
    min = 0
    for i in range(len(list)):
        if list[i] <= list[min]:
            min = i
    return min

