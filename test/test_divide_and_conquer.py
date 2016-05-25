import divide_and_conquer.binary_search as binary_search
import divide_and_conquer.inversions as inversions
import divide_and_conquer.majority_element as majority_element
import divide_and_conquer.points_and_segments as points_and_segments
import divide_and_conquer.sorting as sorting
import pytest


@pytest.mark.timeout(10)  # 10 seconds timeout for binary this tests
class TestBinarySearch:
    @pytest.mark.parametrize("test_input,expected", [
        (([5, 1, 5, 8, 12, 13], [5, 8, 1, 23, 1, 11]), "2 0 -1 0 -1")
    ])
    def test_sample(self, test_input, expected, main_runner):
        result = main_runner(binary_search, test_input)
        assert expected in result


@pytest.mark.skip(reason="TODO")
class TestInversions:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(5, [2, 3, 9, 2, 2])
        inversions.main()
        out, err = capfd.readouterr()
        assert "1" in out


@pytest.mark.skip(reason="TODO")
class TestMajorityElement:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(1, 23, 39)
        majority_element.main()
        out, err = capfd.readouterr()
        assert out == "897\n"


@pytest.mark.skip(reason="TODO")
class TestPointsAndSegments:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(3, [1, 6], [2, 5], [3, 6])
        points_and_segments.main()
        out, err = capfd.readouterr()
        assert "1\n3" in out


@pytest.mark.skip(reason="TODO")
class TestSorting:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(6)
        sorting.main()
        out, err = capfd.readouterr()
        assert "3\n1 2 3" in out
