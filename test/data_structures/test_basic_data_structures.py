import data_structures.basic.check_brackets as check_brackets
import data_structures.basic.tree_height as tree_height

import pytest
import os
import glob


@pytest.mark.timeout(1)  # 1 second timeout for this tests
class TestCheckBrackets:
    def test_one_opening(self, main_runner):
        test_input = ["("]
        expected = "1"
        assert expected in main_runner(check_brackets, test_input)

    def test_one_closing_beginning(self, main_runner):
        test_input = [")[]"]
        expected = "1"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample1(self, main_runner):
        test_input = ["[]"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample2(self, main_runner):
        test_input = ["{}[]"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample3(self, main_runner):
        test_input = ["[()]"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample4(self, main_runner):
        test_input = ["(())"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample5(self, main_runner):
        test_input = ["{[]}()"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample6(self, main_runner):
        test_input = ["{"]
        expected = "1"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample7(self, main_runner):
        test_input = ["{[}"]
        expected = "3"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample8(self, main_runner):
        test_input = ["foo(bar);"]
        expected = "Success"
        assert expected in main_runner(check_brackets, test_input)

    def test_sample9(self, main_runner):
        test_input = ["foo(bar[i);"]
        expected = "10"
        assert expected in main_runner(check_brackets, test_input)

        # def test_provided_input_data(self, main_runner):
        #     files = [f for f in os.listdir('./check_brackets_test_input') if os.path.isfile(f)]
        #     for file in files:
        #         with open(file) as f:
        #             test_input = [f.readline()]
        #             expected = "Success"
        #             assert expected in main_runner(check_brackets, test_input)


@pytest.mark.timeout(3)
class TestTreeHeight:
    def test_sample1(self):
        test_input = [4, -1, 4, 1, 1]
        tree = tree_height.TreeHeight(len(test_input), test_input)
        assert 3 == tree.compute_height()

    def test_sample2(self):
        test_input = [-1, 0, 4, 0, 3]
        tree = tree_height.TreeHeight(len(test_input), test_input)
        assert 4 == tree.compute_height()

        # def test_provided_input_data(self):
        #     files_wildcard = os.path.dirname(__file__) + "/tree_height_test_input/*"
        #     files = glob.glob(files_wildcard)
        #     for file in files:
        #         with open(file) as f:
        #             size = f.readline()
        #             parent = f.readline()
        #             test_input = [int(x) for x in parent.split()]
        #             tree = tree_height.TreeHeight(len(test_input), test_input)
