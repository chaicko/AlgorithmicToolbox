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
        assert expected in main_runner(binary_search, test_input)

    def test_worst_case(self):
        a = [i for i in range(10 ** 5)]
        assert len(a) - 1 == binary_search.binary_search(a, a[-1])

    def test_middle_element_even(self):
        a = [i for i in range(10 ** 5)]
        assert len(a) // 2 == binary_search.binary_search(a, a[len(a) // 2])

    def test_middle_element_odd(self):
        a = [i for i in range(10 ** 5 - 1)]
        assert len(a) // 2 == binary_search.binary_search(a, a[len(a) // 2])

    def test_worst_problem_size(self):
        a = [i for i in range(10 ** 5)]
        for x in range(len(a), len(a) + 10 ** 5):
            assert -1 == binary_search.binary_search(a, x)

    def test_2_grader(self, main_runner):
        test_input = ([10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                      [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        expected = "-1 0 1 2 3 4 5 6 7 8 9 -1"
        assert expected in main_runner(binary_search, test_input)


class TestInversions:
    @pytest.mark.parametrize("test_input,expected", [
        (([5], [2, 3, 9, 2, 9]), "2")
    ])
    def test_samples(self, test_input, expected, main_runner):
        assert expected in main_runner(inversions, test_input)


class TestMajorityElement:
    @pytest.mark.parametrize("test_input,expected", [
        (([5], [2, 3, 9, 2, 2]), "1"),
        (([4], [1, 2, 3, 4]), "0"),
        (([4], [1, 2, 3, 1]), "0")
    ])
    def test_sample(self, test_input, expected, main_runner):
        assert expected in main_runner(majority_element, test_input)

    def test_3_grader(self, main_runner):
        test_input = ([10],
                      [2, 124554847, 2, 941795895, 2, 2, 2, 2, 792755190,
                       756617003])
        expected = "1"
        assert expected in main_runner(majority_element, test_input)

    def test_one_element(self, main_runner):
        test_input = ([1], [1])
        expected = "1"
        assert expected in main_runner(majority_element, test_input)

    def test_two_different_elements(self, main_runner):
        test_input = ([2], [1, 2])
        expected = "0"
        assert expected in main_runner(majority_element, test_input)

    def test_two_equal_elements(self, main_runner):
        test_input = ([2], [2, 2])
        expected = "1"
        assert expected in main_runner(majority_element, test_input)

    def test_worst_case_equals(self, main_runner):
        l = [10 ** 9] * (10 ** 5)
        test_input = (len(l), l)
        expected = "1"
        assert expected in main_runner(majority_element, test_input)

    def test_big_input_majority_corner_case(self, main_runner):
        import random
        l = [random.randint(0, 10 ** 9) for _ in range((10 ** 5) // 2 - 1)] + \
            ([1] * ((10 ** 5) // 2 + 1))
        assert len(l) == 10 ** 5

        test_input = (len(l), l)
        expected = "1"
        assert expected in main_runner(majority_element, test_input)

    def test_big_input_no_majority_corner_case(self, main_runner):
        import random
        l = [random.randint(0, 10 ** 9) for _ in range((10 ** 5) // 2)] + \
            ([1] * ((10 ** 5) // 2))
        assert len(l) == 10 ** 5

        test_input = (len(l), l)
        expected = "0"
        assert expected in main_runner(majority_element, test_input)

    def test_majority_is_biggest(self, main_runner):
        test_input = ([5], [0, 2, 0, 2, 2])
        expected = "1"
        assert expected in main_runner(majority_element, test_input)


@pytest.mark.skip(reason="TODO")
class TestPointsAndSegments:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(3, [1, 6], [2, 5], [3, 6])
        points_and_segments.main()
        out, err = capfd.readouterr()
        assert "1\n3" in out


@pytest.mark.timeout(10)  # 10 seconds timeout for binary this tests
class TestSorting:
    @pytest.mark.parametrize("test_input,expected", [
        (([5], [2, 3, 9, 2, 2]), "2 2 2 3 9")
    ])
    def test_samples(self, test_input, expected, main_runner):
        assert expected in main_runner(sorting, test_input)

    def test_should_sort_inverted_sequence(self, main_runner):
        a = [x for x in reversed(range(1, 10 ** 5 + 1))]
        test_input = (len(a), a)
        expected = " ".join((str(x) for x in reversed(a)))
        assert expected in main_runner(sorting, test_input)

    def test_randomized_quick_sort2_inverted_sequence(self):
        a = [x for x in reversed(range(1, 10 ** 5 + 1))]
        expected = a[::-1]
        sorting.randomized_quick_sort(a, 0, len(a) - 1)
        assert expected == a

    def test_randomized_quick_sort3_inverted_sequence(self):
        a1 = [x for x in reversed(range(1, 10 ** 5 + 1))]
        a2 = list(a1)
        sorting.randomized_quick_sort(a1, 0, len(a1) - 1)
        sorting.randomized_quick_sort3(a2, 0, len(a2) - 1)
        assert a1 == a2

    def test_all_equal_elements(self, main_runner):
        a = [3] * 10 ** 5
        test_input = (len(a), a)
        expected = " ".join((str(x) for x in a))
        assert expected in main_runner(sorting, test_input)

    def test_partition3_basic(self):
        a = [5, 4, 5, 5, 3, 5, 8, 1]
        m1, m2 = sorting.partition3(a, 0, len(a) - 1)
        assert m1 == 3
        assert m2 == 6
        assert a == [1, 4, 3, 5, 5, 5, 5, 8]

    def test_partition3_three_simple(self):
        a = [2, 3, 1]
        expected = list(a)
        m = sorting.partition2(expected, 0, len(expected) - 1)
        m1, m2 = sorting.partition3(a, 0, len(a) - 1)
        assert m1 == m
        assert m2 == m
        assert a == expected

    def test_partition3_reversed(self):
        a = [x for x in reversed(range(1, 10))]
        expected = list(a)
        expected[0], expected[-1] = expected[-1], expected[0]
        m1, m2 = sorting.partition3(a, 0, len(a) - 1)
        assert m1 == len(a) - 1
        assert m2 == len(a) - 1
        assert a == expected

    def test_partition2_reversed(self):
        a = [x for x in reversed(range(1, 10))]
        expected = list(a)
        expected[0], expected[-1] = expected[-1], expected[0]
        m = sorting.partition2(a, 0, len(a) - 1)
        assert m == len(a) - 1
        assert a == expected
