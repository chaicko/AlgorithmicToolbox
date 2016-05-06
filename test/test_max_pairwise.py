from unittest import TestCase
from max_pairwise.max_pairwise_product import *
import random
import heapq


class TestMaxPairwiseProduct(TestCase):

    def test_zero_on_empty_sequence(self):
        assert max_pairwise_prod([]) == 0

    def test_zero_on_one_element_sequence(self):
        assert max_pairwise_prod([1]) == 0

    def test_min_seq(self):
        assert max_pairwise_prod([1, 2]) == 2

    def test_min_seq_zero(self):
        assert max_pairwise_prod([0, 2]) == 0

    def test_min_seq_equal_values(self):
        assert max_pairwise_prod([2, 2]) == 4

    def test_max_seq_simple(self):
        seq = [(i % MAX_VALUE) + 1 for i in range(MAX_SEQ_LEN)]
        assert max_pairwise_prod(seq) == MAX_VALUE * MAX_VALUE

    def test_max_seq_random(self):
        seq = [random.randint(0, MAX_VALUE) for _ in range(MAX_SEQ_LEN)]
        largest = heapq.nlargest(2, seq)
        assert max_pairwise_prod(seq) == largest[0] * largest[1]

    def test_running_time(self):
        pass

    def test_memory_usage(self):
        pass
