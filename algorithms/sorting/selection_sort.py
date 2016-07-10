# -*- coding: utf-8 -*-
""" Implementation of Selection Sort """


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
