# https://www.hackerrank.com/challenges/insertion-sort/problem?isFullScreen=true

import unittest


def merge_sort(arr):
    n = len(arr)
    helper = [0] * n
    return merge_sort_aux(arr, helper, 0, n - 1)


def merge_sort_aux(arr, helper, start, end):
    total = 0
    if start < end:
        mid = (start + end) // 2
        total += merge_sort_aux(arr, helper, start, mid)
        total += merge_sort_aux(arr, helper, mid + 1, end)
        total += merge(arr, helper, start, mid, end)
    return total


def merge(arr, helper, start, mid, end):
    i = start
    while i <= end:
        helper[i] = arr[i]
        i += 1

    total = 0
    helperLeft = start
    helperRight = mid + 1
    current = start
    while helperLeft <= mid and helperRight <= end:
        if helper[helperLeft] <= helper[helperRight]:
            arr[current] = helper[helperLeft]
            helperLeft += 1
        elif helper[helperLeft] > helper[helperRight]:
            arr[current] = helper[helperRight]
            helperRight += 1
            total += (mid - start + 1) - (helperLeft - start)
        current += 1
    while helperLeft <= mid:
        arr[current] = helper[helperLeft]
        helperLeft += 1
        current += 1
    return total


def insertionSortAdvanceAnalysis(arr):
    return merge_sort(arr)


class Testing(unittest.TestCase):

    def test_001(self):
        arr = list(map(int, '1 1 1 2 2'.split(' ')))
        total = insertionSortAdvanceAnalysis(arr)
        self.assertEqual(total, 0)

    def test_002(self):
        arr = list(map(int, '2 1 3 1 2'.split(' ')))
        total = insertionSortAdvanceAnalysis(arr)
        self.assertEqual(total, 4)

    def test_003(self):
        arr = list(map(int, '12 15 1 5 6 14 11'.split(' ')))
        total = insertionSortAdvanceAnalysis(arr)
        self.assertEqual(total, 10)

    def test_004(self):
        arr = list(map(int, '3 5 7 11 9'.split(' ')))
        total = insertionSortAdvanceAnalysis(arr)
        self.assertEqual(total, 1)


if __name__ == '__main__':
    unittest.main()
