import dynprog.edit_distance as ed
import dynprog.knapsack as knapsack
import dynprog.placing_parentheses as placing_parentheses

import pytest


@pytest.mark.timeout(10)  # 10 seconds timeout for this tests
class TestKnapsack:
    @pytest.mark.parametrize("test_input,expected", [
        ((10, [1, 4, 8]), 9)
    ])
    def test_sample(self, test_input, expected):
        W = test_input[0]
        w = test_input[1]
        assert expected == knapsack.optimal_weight(W, w)


@pytest.mark.timeout(5)  # 5 seconds timeout for this tests
class TestEditDistance:
    @pytest.mark.parametrize("test_input,expected", [
        (("ab", "ab"), 0),
        (("short", "ports"), 3),
        (("editing", "distance"), 5)
    ])
    def test_samples(self, test_input, expected):
        in0 = test_input[0]
        in1 = test_input[1]
        assert expected == ed.edit_distance(in0, in1)


@pytest.mark.timeout(5)  # 5 seconds timeout for this tests
class TestPlacingParenthesis:
    @pytest.mark.parametrize("test_input,expected", [
        ("1+5", 6),
        ("5-8+7*4-8+9", 200)
    ])
    def test_samples(self, test_input, expected):
        assert expected == placing_parentheses.get_maximum_value(test_input)
