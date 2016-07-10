import random
import unittest
from ..sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort


class TestBubbleSort(unittest.TestCase):
    """
    Tests Bubble sort on a small range from 0-9
    """
    def test_bubblesort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        bubble_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestInsertionSort(unittest.TestCase):
    """
    Tests Insertion sort on a small range from 0-9
    """
    def test_insertionsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        insertion_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestSelectionSort(unittest.TestCase):
    """
    Tests Selection sort on a small range from 0-9
    """
    def test_selectionsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        selection_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestMergeSort(unittest.TestCase):
    """
    Tests Merge sort on a small range from 0-9,
    also tests merge function included in merge sort
    """
    def test_mergesort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        merge_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

    def test_merge(self):
        self.seq1 = range(5)
        self.seq2 = range(5, 10)
        self.seq = merge_sort.merge(self.seq1, self.seq2)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestQuickSort(unittest.TestCase):
    """
    Tests Quick sort on a small range from 0-9
    """
    def test_quicksort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        quick_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

