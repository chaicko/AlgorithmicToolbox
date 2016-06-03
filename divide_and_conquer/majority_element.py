# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    # First divide the Array in 2 halves, and call recursively on this.
    # These calls are the 2*T(n/2) part (log n) of the master theorem
    half = (right - left) // 2
    ml = get_majority_element(a, left, left + half)
    mr = get_majority_element(a, left + half, right)

    # ml/mr at this point are numbers or -1. Because -1 is not part of the
    # problem we can safely compare the numbers with the part of the array
    # that we are evaluating at this point (a[left:right)
    mlc = mrc = 0
    for v in a[left:right]:
        if v == ml:
            mlc += 1
        if v == mr:
            mrc += 1

    # Finally if the count adds up to more than the half of the array being
    # evaluated, then return that majority number
    if mlc > half:
        return ml
    if mrc > half:
        return mr

    # If is not a majority number, then return not found
    return -1


def get_majority_element_linear(a, left, right):
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
