""" Implementation of Bubble Sort. """


def sort(seq):

    for x in seq:
        tmp = 0
        for n in range(1, len(seq)):
            tmp = seq[n]
            if seq[n] < seq[n-1]:
                seq[n] = seq[n-1]
                seq[n-1] = tmp

    return seq
