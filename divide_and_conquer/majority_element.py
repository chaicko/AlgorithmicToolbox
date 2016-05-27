# Uses python3
import sys


def get_majority_element_sorted(a, left, right):
    sorted_a = sorted(a)
    size = right - left
    half = size // 2

    # Check the first half of the array. If the same element is at the
    # beginning and the middle, then is a majority
    if sorted_a[left] == sorted_a[left + half]:
        return sorted_a[left]

    # Check again but for biggest sorted element, take care of indexes
    sub = 1 if size % 2 == 0 else 0
    if sorted_a[left + half - sub] == sorted_a[right - 1]:
        return sorted_a[right - 1]

    return -1


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # size = right - left
    # half = size // 2
    # r1 = get_majority_element(a, left, left + half)
    # r2 = get_majority_element(a, left + half, right)
    # if r1 == r2:
    #     return r1
    return -1


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_sorted(a, 0, n) != -1:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
