# -*- coding: utf-8 -*-
""" Implementation of Quick Sort """


def sort(seq):

    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left = sort([x for x in seq[1:] if x < pivot])
        right = sort([x for x in seq[1:] if x >= pivot])
        return left + [pivot] + right
