# https://www.hackerrank.com/contests/justcode/challenges/length-of-the-longest-non-decreasing-sequence-
import unittest


def getLongestNonDecreasingSequence(arr):
    n = len(arr)
    longest_non_decreasing_sequence = 1
    i = 1
    running_longest_non_decreasing_sequence = 1
    while i < n:
        if arr[i - 1] < arr[i]:
            running_longest_non_decreasing_sequence += 1
        else:
            if running_longest_non_decreasing_sequence > longest_non_decreasing_sequence:
                longest_non_decreasing_sequence = running_longest_non_decreasing_sequence
            running_longest_non_decreasing_sequence = 1
        i += 1
    if running_longest_non_decreasing_sequence > longest_non_decreasing_sequence:
        longest_non_decreasing_sequence = running_longest_non_decreasing_sequence
    return longest_non_decreasing_sequence


class Testing(unittest.TestCase):

    def test_0(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '6 1 2 3 4 9'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 5)

    def test_1(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '1 2 3 4 5'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 5)

    def test_2(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '6 5 4 3 2 1'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 1)

    def test_3(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '7 8 9 5 6 4 7'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 3)

    def test_4(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '45 1 2 4 5 6 7 8 2 5 9'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 7)

    def test_5(self):
        longest_non_decreasing_sequence = getLongestNonDecreasingSequence(
            list(map(int, '7 4 5 8 1'.split(' '))))
        self.assertEqual(longest_non_decreasing_sequence, 3)


if __name__ == '__main__':
    unittest.main()
