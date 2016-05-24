# Uses python3
import sys


def optimal_summands(n):
    summands = []
    k = n
    l = 1
    # O(logn) algorithm
    while k > 0:
        s = k if k <= 2 * l else l
        summands.append(s)
        k -= s
        l += 1
    return summands


def main():
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

if __name__ == '__main__':
    main()
