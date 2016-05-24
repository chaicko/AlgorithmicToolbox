# Uses python3
import sys


def get_change(n):
    tens = n // 10
    n -= tens * 10
    fives = n // 5
    n -= fives * 5
    ones = n
    return tens + fives + ones


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
