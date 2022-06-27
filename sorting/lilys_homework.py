# https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

import unittest


def count_swaps(arr, d):
    i, swaps = 0, 0
    while i < len(arr):
        loc = d[arr[i]]
        if loc == i:
            i += 1
            continue
        arr[i], arr[loc] = arr[loc], arr[i]
        swaps += 1
    return swaps


def lilysHomework(arr):
    sorted_arr = sorted(arr)

    forward_d = {v: i for i, v in enumerate(sorted_arr)}
    backward_d = {v: i for i, v in enumerate(reversed(sorted_arr))}

    return min(count_swaps(arr.copy(), forward_d), count_swaps(arr.copy(), backward_d))


class Testing(unittest.TestCase):

    def test_001(self):
        arr = list(map(int, '2 5 3 1'.split(' ')))
        total = lilysHomework(arr)
        self.assertEqual(total, 2)

    def test_002(self):
        arr = list(map(int, '3 4 2 5 1'.split(' ')))
        total = lilysHomework(arr)
        self.assertEqual(total, 2)


if __name__ == '__main__':
    unittest.main()
