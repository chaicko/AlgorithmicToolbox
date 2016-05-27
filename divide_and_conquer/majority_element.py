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

    # Implementing it using a dictionary in O(n) (actually O(2*n))
    d = {}

    # The Dictionary value are { number: count } where we just count the number
    # of times a given number of the sequence appear
    for num in a:
        try:
            d[num] += 1
        except KeyError:
            d[num] = 1

    # Then we iterate over the all the keys of the dictionary (numbers). If
    # the count of each key is more than half the size of the array then the
    # number is a majority element and we return its value
    for k, v in d.items():
        if v > len(a) / 2:
            return k

    return -1


def main():
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
