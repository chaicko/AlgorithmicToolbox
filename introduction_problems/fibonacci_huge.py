# Uses python3
import sys

FIBO_HUGE_MAX_MOD = 10 ** 5
FIBO_HUGE_MAX_NUM = 10 ** 18


def fibseq(mod):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b) % mod


def fib_seq_mod(m):
    """Returns the fibonacci modulo 'm' periodic sequence.

    This is quite slow actually and needs to be enhanced.
    :param m: modulo
    :return: sequence of numbers that form the Pisano period (modulo m)
    """
    seq = []
    for f in fibseq(m):
        seq.append(f)  # append fibonacci mod m to a list
        if len(seq) > 3 and seq[:2] == seq[len(seq) - 2:]:
            return seq[:len(seq) - 2]


def get_fibonaccihuge(n, m):
    seq = []
    for i, f in enumerate(fibseq(m)):
        seq.append(f)  # append fibonacci mod m to a list

        # search for the [0, 1] period boundary (is unique)
        if len(seq) > 3 and seq[:2] == seq[len(seq) - 2:]:
            # if [0, 1] is found, remove top two elements of the
            # sequence because those are not part of the period
            # i.e. for m == 2, seq = [0, 1, 1, 0, 1] at this point
            del seq[-2:]
            break

        # quit the loop if the current sequence is longer or
        # equal to the input n because we compute the remainder
        # of this number divided by the sequence length, and if
        # n is less than the length of the sequence then the number
        # is just the required remainder
        if i >= n:
            break

    seq_len = len(seq)
    rem = n % seq_len
    return seq[rem]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
