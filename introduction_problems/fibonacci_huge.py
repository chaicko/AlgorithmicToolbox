# Uses python3
import sys

FIBO_HUGE_MAX_MOD = 10 ** 5
FIBO_HUGE_MAX_NUM = 10 ** 18


def get_fibonaccihuge(n, m):
    if n < 1:
        return n
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, (a + b) % m
    return b

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
