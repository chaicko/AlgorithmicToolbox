from unittest import TestCase
from max_pairwise.Solver import Solver
from nose.tools import eq_


class TestSolver(TestCase):
    def test_negative_discr(self):
        s = Solver()
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    def test_demo(self):
        pass
        #self.fail()
