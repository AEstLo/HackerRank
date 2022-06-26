# https://www.hackerrank.com/challenges/countingsort4?isFullScreen=true

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    result = [[], []]
    n = len(arr)
    replace_before = n // 2
    for i in range(n):
        elem = arr[i]
        x = int(elem[0])
        while x >= len(result):
            result.append([])
        if i < replace_before:
            char = '-'
        else:
            char = elem[1]
        result[x].append(char)
    i = 0
    while i < len(result):
        for elem in result[i]:
            print(elem, end=' ')
        i += 1


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
