# Uses python3
MAX_SEQ_LEN = 2 * (10 ** 5)
MAX_VALUE = 10 ** 5


def max_pairwise_prod(a: list) -> int:
    """Computes the Maximum Pairwise Product in a list of integers.

    Finds the maximum pairwise product, that is, the largest integer that can
    be obtained by multiplying two different elements from the sequence a
    (or, more formally, max(a[i] * a[j]) where i != j and i,j <= len(a)).

    The sequence a has at least 2 elements and at most 2 * 10 ^ 5. Each element
    of the sequence is an integer number n where 0 <= n <= 10 ^ 5.

    For example:

    >>> print(max_pairwise_prod([1, 4, 20, 30, 70]))
    2100

    :param a: The list of positive integers.
    :return: max(a[i] * a[j]) where i != j and i,j <= len(a)
    """
    result = 0
    n = len(a)
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]
    return result


if __name__ == '__main__':
    m = int(input())
    arr = [int(x) for x in input().split()]
    assert(len(arr) == m)
    assert(m <= MAX_SEQ_LEN)
    res = max_pairwise_prod(arr)
    print(res)

