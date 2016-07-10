# -*- coding: utf-8 -*-
"""
    selection_sort.py

    This module implements selection sort on an unsorted list and returns a sorted list.

    Selection Sort Overview:
    ------------------------
    Uses in-place comparision to sort the list

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity:  O(n^2)

    Space Complexity: O(n)

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Selection_sort

    selection_sort.sort(list) -> sorted_list
"""


# 固定位置找元素
def sort(seq):

    for i in range(0, len(seq)):
        minat = i
        minum = seq[i]
        for j in range(i, len(seq)):
            if seq[j] < minum:
                minum = seq[j]
                minat = j
        tmp = seq[i]
        seq[i] = minum
        seq[minat] = tmp
    return seq
