import graphs.reachability as reach
import graphs.connected_components as cc
import graphs.acyclicity as ac
import graphs.toposort as topo
import pytest


@pytest.mark.timeout(5)  # 5 seconds timeout for basic graphs
class TestReachability:
    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4''', ([[1, 3], [0, 2], [1, 3], [2, 0]], 0, 3)),
        ('''
        4 2
        1 2
        3 2
        1 4''', ([[1], [0, 2], [1], []], 0, 3)),
    ])
    def test_parse_input(self, test_input, expected):
        assert reach.parse_input(test_input) == expected

    def test_min_no_reach(self):
        assert reach.reach([[], []], 0, 1) == 0

    def test_min_reach(self):
        assert reach.reach([[1], [0]], 0, 1) == 1

    @pytest.mark.skip("Complete this one!")
    def test_longest_path(self):
        # Longest path is the longest hops from frist vertex to last
        adj = [[] for _ in range(reach.MAX_VERTICES)]
        adj[0].append(1)
        adj[-1].append(len(adj)-2)
        for i in range(1, len(adj)-1):
            pass

        pass

    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 4
        1 2
        3 2
        4 3
        1 4
        1 4''', 1),
        ('''
        4 2
        1 2
        3 2
        1 4''', 0),
    ])
    def test_sample(self, test_input, expected):
        assert reach.reach(*reach.parse_input(test_input)) == expected


@pytest.mark.timeout(5)  # 5 seconds timeout for basic graphs
class TestConnectedComponents:
    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 2
        1 2
        3 2
        1 2''', ([[1], [0, 2], [1], []])),
    ])
    def test_parse_input(self, test_input, expected):
        assert cc.parse_input(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 2
        1 2
        3 2
        1 2''', 2,)
    ])
    def test_sample(self, test_input, expected):
        assert cc.number_of_components(cc.parse_input(test_input)) == expected


@pytest.mark.timeout(5)  # 5 seconds timeout for basic graphs
class TestAcyclicity:

    def test_graph_bad_inpput(self):
        with pytest.raises(ValueError):
            ac.Graph(None)

    def test_graph_adj_input(self):
        adj_info_str = '''
        4 2
        1 2
        3 2
        1 2'''
        adj_info_list = [[1], [0, 2], [1], []]
        g1 = ac.Graph(adj_info_str, directed=False)
        g2 = ac.Graph(adj_info_list)
        assert g1.adj == g2.adj
        assert g1.adj == adj_info_list

    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 4
        1 2
        4 1
        2 3
        3 1''', 1,),
        ('''
        5 7
        1 2
        2 3
        1 3
        3 4
        1 4
        2 5
        3 5''', 0,),
    ])
    def test_sample(self, test_input, expected):
        assert ac.acyclic(ac.Graph(test_input)) == expected


@pytest.mark.timeout(10)  # 10 seconds timeout for basic graphs
class TestToposort:

    def test_graph_bad_inpput(self):
        with pytest.raises(ValueError):
            ac.Graph(None)

    @pytest.mark.parametrize("test_input,expected", [
        ('''
        4 3
        1 2
        4 1
        3 1''', "4 3 1 2",),
        ('''
        4 1
        3 1''', "4 3 2 1",),
        ('''
        5 7
        2 1
        3 2
        3 1
        4 3
        4 1
        5 2
        5 3''', "5 4 3 2 1",),
    ])
    def test_sample(self, test_input, expected):
        assert topo.toposort_str(test_input, directed=True) == expected
