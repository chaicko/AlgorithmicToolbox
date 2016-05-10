from unittest import TestCase
from introduction_problems.fib import *
from utils.decorators import *
from nose.tools import eq_


def fib(n):
    a, b = 0, 1
    while a <= n:  # First iteration:
        yield a  # yield 0 to start with and then
        a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


class TestSmallFibonacci(TestCase):
    def test_fib_0_is_0(self):
        eq_(calc_fib(0), 0)

    def test_fib_1_is_1(self):
        eq_(calc_fib(1), 1)

    def test_fib_first_45(self):
        for index, fibo in enumerate(fib(45)):
            res = calc_fib(index)
            eq_(res, fibo, "fib(%d)=%d != %d" % (index, res, fibo))
