# Uses python3
import sys


def get_majority_element_sorted(a, left, right):
    sorted_a = sorted(a)
    cmp_idx = right // 2
    if right % 2 == 0:
        cmp_idx += 1
    if sorted_a[left] == sorted_a[cmp_idx]:
        return 1

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
