#Uses python3
import sys


def min_dot_product(a, b):
    a = sorted(a)
    b = sorted(b, reverse=True)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))


if __name__ == '__main__':
    main()
