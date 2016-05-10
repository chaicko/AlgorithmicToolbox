# Uses python3
import sys

FIBONACCI_LAST_DIGIT_MAX_VALUE = 10 ** 7


def get_fibonacci_last_digit(n):
    if n < 1:
        return n
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, (a + b) % 10
    return b


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
