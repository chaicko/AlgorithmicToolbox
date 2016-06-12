import data_structures.basic.check_brackets as check_brackets

import pytest


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
