# Uses python3
import sys

MAX_GCD_OPERAND_VALUE = 2 * 10 ** 9


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
