# https://www.hackerrank.com/challenges/kingdom-division?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#


def kingdomDivision(n, roads):
    if n == 0:
        return 0
    total = 2  # All to the same son

    adjacentMatrix = {i: set() for i in range(1, n + 1)}
    for road in roads:
        adjacentMatrix[road[0]].add(road[1])
        adjacentMatrix[road[1]].add(road[0])

    visited = set()
    while len(visited) < n:
        for k, v in adjacentMatrix.items():
            if len(v - visited) == 1:
                visited.add(k)
                total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    result = kingdomDivision(n, roads)

    fptr.write(str(result) + '\n')

    fptr.close()
