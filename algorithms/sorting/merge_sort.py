"""
    merge_sort.py

    This module implements merge sort on an unsorted list and returns a sorted list.

    Merge Sort Overview:
    ------------------------
    Uses divide and conquer to recursively divide and sort the list

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n log n) average, O(n log n) worst case

    Space Complexity: O(n)

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

    merge_sort.sort(list) -> sorted_list
"""


def merge(left, right):
    result = []
    m, n = 0, 0
    while m < len(left) and n < len(right):
        if left[m] <= right[n]:
            result.append(left[m])
            m += 1
        else:
            result.append(right[n])
            n += 1

    result += left[m:]
    result += right[n:]
    return result


def sort(seq):
    if len(seq) <= 1:
        return seq

    middle = len(seq) / 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)

