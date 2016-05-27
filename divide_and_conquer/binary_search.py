# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)
    while left <= right:
        mid = left + (right - left) // 2
        if mid == len(a):
            return -1
        d = a[mid] - x
        if d == 0:
            return mid
        elif d > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')


if __name__ == '__main__':
    main()
