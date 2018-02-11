# Uses python3
import sys
sys.setrecursionlimit(200000)


class Graph:

    BACK_EDGE, CROSS_EDGE, FORWARD_EDGE, TREE_EDGE = 0, 1, 2, 3

    @staticmethod
    def parse_adj_info(adj_info, directed):
        data = list(map(int, adj_info.strip().split()))
        n, m = data[0:2]
        data = data[2:]
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
        adj = [[] for _ in range(n)]
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            if not directed:
                adj[b - 1].append(a - 1)
        return adj

    def __init__(self, adj_info, directed=True,
                 previsit=lambda self, v: None,
                 postvisit=lambda self, v: None,
                 process_edge=lambda self, u, v: None):
        if isinstance(adj_info, str):
            self.adj = Graph.parse_adj_info(adj_info, directed)
        elif isinstance(adj_info, list):
            self.adj = adj_info
        else:
            raise ValueError('adj_info should be either an adjacency list or a string')

        self.directed = directed
        self.initialize()
        self.previsit = previsit
        self.postvisit = postvisit
        self.process_edge = process_edge

    def initialize(self):
        self.visited = [False] * len(self.adj)
        self.processed = list(self.visited)
        self.parent = [None] * len(self.adj)
        self.cc = 0
        self.clock = 0
        self.entry_time = [0] * len(self.adj)
        self.exit_time = list(self.entry_time)
        self.finish = False  # helper variable
        self.scc = list(self.parent)
        self.low = [i for i in range(len(self.adj))]

    def explore(self, v):
        if self.finish:
            return  # allow early termination

        self.visited[v] = True

        # Tick the entry time
        self.clock += 1
        self.entry_time[v] = self.clock
        self.previsit(self, v)

        for u in self.adj[v]:
            if not self.visited[u]:
                self.parent[u] = v
                self.process_edge(self, v, u)  # do something if wanted
                self.explore(u)
            elif self.directed or (not self.processed[u] and self.parent[v] != u):
                # XXX see "The Algorithm Design Manual", section 5.9
                # Processing of back/forward edges
                self.process_edge(self, v, u)

            if self.finish:
                return  # allow early termination

        self.postvisit(self, v)
        # Tock the exit time
        self.clock += 1
        self.exit_time[v] = self.clock
        self.processed[v] = True

    def dfs(self, ordered_vertices=None):
        if ordered_vertices is None:
            ordered_vertices = range(len(self.adj))
        for i in ordered_vertices:
            if not self.visited[i]:
                self.explore(i)
                self.cc += 1

    def edge_class(self, x, y):
        if self.parent[y] == x:
            return Graph.TREE_EDGE
        if self.visited[y] and not self.processed[y]:
            return Graph.BACK_EDGE
        if self.processed[y] and self.entry_time[y] > self.entry_time[x]:
            return Graph.FORWARD_EDGE
        if self.processed[y] and self.entry_time[y] < self.entry_time[x]:
            return Graph.CROSS_EDGE

        raise RuntimeError('Unclassified edge {}'.format((x, y)))


def num_scc_skiena(adj_info):
    """Counts strongly connected components by using more data structures.

    Solution taken from "The Algorithm Design Manual", Skiena, and
    rewritten in Python.

    Note that this one has a worse McCabe number than the other (15).
    """
    active = list()
    cc = 0

    def pop_component(g, v):
        nonlocal cc
        cc += 1
        g.scc[v] = cc
        while True:
            t = active.pop()
            if t == v:
                break
            g.scc[t] = cc

    def process_vertex_early(g, v):
        active.append(v)

    def process_vertex_late(g, v):
        if g.low[v] == v:  # edge (parent[v], v) cuts off scc
            pop_component(g, v)

        if g.parent[v] is not None:  # only if v is not the root
            if g.entry_time[g.low[v]] < g.entry_time[g.low[g.parent[v]]]:
                g.low[g.parent[v]] = g.low[v]

    def process_edge(g, x, y):
        edge_class = g.edge_class(x, y)
        if edge_class == Graph.BACK_EDGE:
            if g.entry_time[y] < g.entry_time[g.low[x]]:
                g.low[x] = y
        if edge_class == Graph.CROSS_EDGE:
            if g.scc[y] is None:  # component not yet assigned
                if g.entry_time[y] < g.entry_time[g.low[x]]:
                    g.low[x] = y

    graph = Graph(adj_info, directed=True, previsit=process_vertex_early,
                  postvisit=process_vertex_late, process_edge=process_edge)
    graph.dfs()
    return cc


def num_scc_rev(adj_info):
    """Counts strongly connected components by revered Graph.

    This solution is slightly less performand then Skiena:

    This one used: (Max time used: 0.12/5.00, max memory used: 11837440/536870912.)
    while Skiena's (Max time used: 0.10/5.00, max memory used: 11833344/536870912.)
    """
    order = list()

    def push_vertex(g, v):
        order.append(v)

    graph = Graph(adj_info)
    rev_graph = Graph(reverse_adj(graph.adj), postvisit=push_vertex)
    rev_graph.dfs()  # DFS on reverse generates the post-ordering

    graph.dfs(ordered_vertices=reversed(order))  # DFS in graph on provided order
    return graph.cc


def reverse_adj(adj):
    rev = [[] for _ in range(len(adj))]
    for i, l in enumerate(adj):
        for v in l:
            rev[v].append(i)
    return rev


if __name__ == '__main__':
    #  print(num_scc_skiena(sys.stdin.read()))
    print(num_scc_rev(sys.stdin.read()))
