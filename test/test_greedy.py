from unittest import TestCase
from greedy.change import get_change
from greedy.fractional_knapsack import get_optimal_value


class TestChange(TestCase):
    def test_sample1(self):
        assert get_change(2) == 2

    def test_sample2(self):
        assert get_change(28) == 6

    def test_change_of_999(self):
        assert get_change(999) == 99 + 1 + 4

    def test_change_all(self):
        for i in range(1, 10 ** 3 + 1):
            n = i
            coins = 0
            while 0 < n:
                if n >= 10:
                    tens = n // 10
                    n -= tens * 10
                    coins += tens
                    continue
                if n >= 5:
                    fives = n // 5
                    n -= fives * 5
                    coins += fives
                    continue
                coins += n
                n = 0

            assert get_change(i) == coins


class TestFractionalKnapsack(TestCase):
    def test_sample1(self):
        assert get_optimal_value(50, [60, 100, 120], [20, 50, 30]) == 180.0000

    def test_sample2(self):
        assert get_optimal_value(10, [60], [30]) == 166.6667
