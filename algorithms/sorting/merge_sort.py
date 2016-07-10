""" Implementation of Merge Sort. """


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

