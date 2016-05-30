# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l  # count the lower bound
    k = 0  # upper bound is j + k
    for i in range(l + 1, r + 1):
        # first add elements to the first partition, just like partition2
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
            if k > 0:  # We remove an element of the middle partition
                k -= 1
        # now add elements to the middle partition
        if a[i] == x:
            k += 1
            a[i], a[j + k] = a[j + k], a[i]
    a[l], a[j] = a[j], a[l]
    return j, j + k


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1 - 1)
    randomized_quick_sort3(a, m2 + 1, r)


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


if __name__ == '__main__':
    main()
