# Uses python3
import sys

FIBO_HUGE_MAX_MOD = 10 ** 5
FIBO_HUGE_MAX_NUM = 10 ** 18


def fibseq():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_seq_mod(m):
    """Returns the fibonacci modulo 'm' periodic sequence.
    :param m: modulo
    :return: sequence of numbers that form the Pisano period (modulo m)
    """
    seq = []
    first_period = seq
    period_len = 0
    for i, f in enumerate(fibseq()):
        fm = f % m
        seq.append(fm)  # append fibonacci mod m to a list
        first_period = seq[:period_len]  # tentative first period
        second_period = seq[period_len:i]  # second period to compare
        second_period_len = i - period_len
        if period_len != 0 and first_period == second_period:
            break
        if fm == seq[0] and second_period_len >= period_len:
            period_len = i

    return first_period


def get_fibonaccihuge(n, m):
    seq_mod = fib_seq_mod(m)
    seq_mod_len = len(seq_mod)
    rem = n % seq_mod_len
    return seq_mod[rem]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
