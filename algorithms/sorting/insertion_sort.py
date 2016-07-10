# -*- coding: utf-8 -*-
""" Implementation of Insertion Sort"""


# 固定元素找位置
def sort(seq):

    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[hole-1] > item:
            seq[hole] = seq[hole - 1]
            hole -= 1
        seq[hole] = item
    return seq
