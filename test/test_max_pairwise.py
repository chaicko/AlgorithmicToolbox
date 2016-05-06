from unittest import TestCase
from max_pairwise.max_pairwise_product import *
import random


class TestMaxPairwiseProduct(TestCase):

    def test_min_seq(self):
        assert max_pairwise_prod([1, 2]) == 2

    def test_min_seq_zero(self):
        assert max_pairwise_prod([0, 2]) == 0

    def test_max_seq_simple(self):
        seq = [(i % MAX_VALUE) + 1 for i in range(MAX_SEQ_LEN)]
        assert max_pairwise_prod(seq) == MAX_VALUE * MAX_VALUE
