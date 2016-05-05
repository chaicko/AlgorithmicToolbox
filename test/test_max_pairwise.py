from unittest import TestCase
from max_pairwise.max_pairwise_product import *
import random


class TestMaxPairwiseProduct(TestCase):

    def test_min_seq(self):
        assert max_pairwise_prod([1, 2]) == 2

    def test_min_seq_zero(self):
        assert max_pairwise_prod([0, 2]) == 0

    def test_max_seq_simple(self):
        seq = [0] * MAX_SEQ_LEN
        seq[0] = 1
        seq[1] = 2
        assert max_pairwise_prod(seq) == 2
