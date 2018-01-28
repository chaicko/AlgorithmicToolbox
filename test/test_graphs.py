import graphs.reachability as reach
import pytest


@pytest.mark.timeout(5)  # 5 seconds timeout for basic graphs
class TestReachability:
    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4''', ([[1, 3], [0, 2], [1, 3], [2, 0]], 0, 3)),
        ('''
        4 2
        1 2
        3 2
        1 4''', ([[1], [0, 2], [1], []], 0, 3)),
    ])
    def test_parse_input(self, test_input, expected):
        assert reach.parse_input(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4''', 1),
        ('''
        4 2
        1 2
        3 2
        1 4''', 0),
    ])
    def test_sample(self, test_input, expected):
        assert reach.reach(*reach.parse_input(test_input)) == expected
