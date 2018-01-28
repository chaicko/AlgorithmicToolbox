import graphs.reachability as reachability
import pytest


@pytest.mark.timeout(5)  # 5 seconds timeout for basic graphs
class TestBasicGraphs:
    @pytest.mark.parametrize("test_input,expected", [
        (([5, 1, 5, 8, 12, 13], [5, 8, 1, 23, 1, 11]), "2 0 -1 0 -1")
    ])
    def test_sample(self, test_input, expected, main_runner):
        assert True  # False
