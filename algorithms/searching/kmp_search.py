"""
    kmp_search.py

    This module implements kmp search on a sorted list.

    KMP Search Overview:
    ------------------------
    Uses a prefix function to reduce the searching time.

    Pre: a string > substring.

    Post: returns a list of indices where the substring was found.

    Time Complexity:  O(n + k), where k is the substring to be found

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

    kmp_search.search(sorted_list) -> list[integers]
    kmp_search.search(sorted_list) -> list[empty]
"""


def search(string, word):
    word_length = len(word)
    string_length = len(string)
    offsets = []

    # check to make sure string is longer than substring
    if word_length > string_length:
        return offsets

    prefix = compute_prefix(word)
    # q is the number of characters matched
    q = 0

    for index, letter in enumerate(string):
        while q > 0 and word[q] != letter:
            q = prefix[q - 1] # next character does not match
        if word[q] == letter:
            q += 1
        if q == word_length:
            offsets.append(index - word_length + 1)
            # look for next match
            q = prefix[q - 1]
    return offsets


def compute_prefix(word):
    word_length = len(word)
    prefix = [0] * word_length
    k = 0

    for q in xrange(1, word_length):
        while k > 0 and word[k] != word[q]:
            k = prefix[k - 1]

        if word[k + 1] == word[q]:
            k += 1
        prefix[q] = k
    return prefix
