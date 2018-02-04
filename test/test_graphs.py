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

    def test_min_no_reach(self):
        assert reach.reach([[], []], 0, 1) == 0

    def test_min_reach(self):
        assert reach.reach([[1], [0]], 0, 1) == 1

    @pytest.mark.skip("Complete this one!")
    def test_longest_path(self):
        # Longest path is the longest hops from frist vertex to last
        adj = [[] for _ in range(reach.MAX_VERTICES)]
        adj[0].append(1)
        adj[-1].append(len(adj)-2)
        for i in range(1, len(adj)-1):
            pass

        pass

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
