from unittest import TestCase
from introduction_problems.fib import calc_fib
from introduction_problems.fibonacci_last_digit import \
    get_fibonacci_last_digit, FIBONACCI_LAST_DIGIT_MAX_VALUE
from introduction_problems.gcd import gcd
from introduction_problems.lcm import lcm
from introduction_problems.fibonacci_huge import get_fibonaccihuge, \
    FIBO_HUGE_MAX_MOD, FIBO_HUGE_MAX_NUM


def fib(n):
    a, b = 0, 1
    while a <= n:  # First iteration:
        yield a  # yield 0 to start with and then
        a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


class TestSmallFibonacci(TestCase):
    def test_fib_0_is_0(self):
        assert calc_fib(0) == 0

    def test_fib_1_is_1(self):
        assert calc_fib(1) == 1

    def test_fib_first_45(self):
        for index, fibo in enumerate(fib(45)):
            res = calc_fib(index)
            assert res == fibo


class TestFibonacciLastDigit(TestCase):
    def test_fib_0_is_0(self):
        assert get_fibonacci_last_digit(0) == 0

    def test_fib_1_is_1(self):
        assert get_fibonacci_last_digit(1) == 1

    def test_fib_all(self):
        for i, f in enumerate(fib(FIBONACCI_LAST_DIGIT_MAX_VALUE)):
            r = get_fibonacci_last_digit(i)
            c = f % 10
            assert r == c


class TestGCD(TestCase):
    def test_sample1(self):
        assert gcd(18, 35) == 1

    def test_sample2(self):
        assert gcd(28851538, 1183019) == 17657

    def test_max_values(self):
        assert gcd(2000000000, 1999999999) == 1


class TestLCM(TestCase):
    def test_sample1(self):
        l = lcm(6, 8)
        assert not isinstance(l, float)
        assert l == 24

    def test_sample2(self):
        l = lcm(28851538, 1183019)
        assert not isinstance(l, float)
        assert l == 1933053046


class TestHugeFibonacci(TestCase):
    def test_fibonaccihuge_0_is_0(self):
        assert get_fibonaccihuge(0, 10) == 0

    def test_fibonaccihuge_1_is_1(self):
        assert get_fibonaccihuge(1, 10) == 1
