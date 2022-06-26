# https://www.hackerrank.com/challenges/construct-the-array?isFullScreen=true

import os

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#


def countArray(n, k, x):
    mod = 10 ** 9 + 7
    ends_with_one = 1
    not_ends_with_one = 0
    for __ in range(2, n + 1):
        new_ends_with_one = not_ends_with_one * (k-1)
        new_not_ends_with_one = ends_with_one + not_ends_with_one * (k - 2)
        ends_with_one = new_ends_with_one % mod
        not_ends_with_one = new_not_ends_with_one % mod
    return ends_with_one if x == 1 else not_ends_with_one


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
