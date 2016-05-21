from greedy.change import get_change
import greedy.dot_product as dot_product
import greedy.fractional_knapsack as fractional_knapsack


class TestChange:
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


class TestFractionalKnapsack:
    def test_sample1(self):
        assert fractional_knapsack.get_optimal_value(50, [20, 50, 30],
                                                     [60, 100, 120]) == 180.0000

    def test_sample2(self):
        assert fractional_knapsack.get_optimal_value(10, [30], [500]) == (
        500 / 3)

    def test_empty_knapsack(self):
        assert fractional_knapsack.get_optimal_value(0, [30], [500]) == 0.0

    def test_items_without_value(self):
        assert fractional_knapsack.get_optimal_value(100, [30, 30, 30],
                                                     [0, 0, 0]) == 0.0

    def test_knapsack_holds_all_items(self):
        assert fractional_knapsack.get_optimal_value(100, [30, 30, 30],
                                                     [10, 10, 10]) == 30.0

    def test_knapsack_holds_all_items_except_last(self):
        assert fractional_knapsack.get_optimal_value(50, [20, 20, 20],
                                                     [10, 10, 10]) == 25.0

    def test_knapsack_holds_all_items_except_last_stdin(self, mock_stdin,
                                                        capfd):
        mock_stdin.setvalue([3, 50], [10, 20], [10, 20], [10, 20])
        fractional_knapsack.main()
        out, err = capfd.readouterr()
        assert "25.0000" in out


class TestDotProduct:
    def test_sample1(self, mock_stdin, capfd):
        mock_stdin.setvalue(1, 23, 39)
        dot_product.main()
        out, err = capfd.readouterr()
        assert out == "897\n"

    def test_sample2(self, mock_stdin, capfd):
        mock_stdin.setvalue(3, [1, 3, -5], [-2, 4, 1])
        dot_product.main()
        out, err = capfd.readouterr()
        assert out == "-25\n"
