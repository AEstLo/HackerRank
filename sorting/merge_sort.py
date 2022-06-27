import random
import unittest


def merge_sort(arr):
    n = len(arr)
    helper = [0] * n
    merge_sort_aux(arr, helper, 0, n - 1)
    return


def merge_sort_aux(arr, helper, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_aux(arr, helper, start, mid)
        merge_sort_aux(arr, helper, mid + 1, end)
        merge(arr, helper, start, mid, end)


def merge(arr, helper, start, mid, end):
    i = start
    while i <= end:
        helper[i] = arr[i]
        i += 1

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
        current += 1
    while helperLeft <= mid:
        arr[current] = helper[helperLeft]
        helperLeft += 1
        current += 1
    return


class Testing(unittest.TestCase):

    def test_100_list_created_randomly(self):
        # Generate X random numbers between 1 and 2000
        for i in range(5000, 5100):
            randomlist = random.sample(range(1, 6000), i)
            sorted_randomlist = sorted(randomlist)
            merge_sort(randomlist)
            self.assertEqual(sorted_randomlist, randomlist)


if __name__ == '__main__':
    unittest.main()
