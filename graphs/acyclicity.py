# Uses python3
import sys


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
    def __init__(self, adj_info, directed=True):
        if isinstance(adj_info, str):
            self.adj = Graph.parse_adj_info(adj_info, directed)
        elif isinstance(adj_info, list):
            self.adj = adj_info
        else:
            raise ValueError('adj_info should be either an adjacency list or a string')

        self.directed = directed
        self.initialize()

    def initialize(self):
        self.visited = [False] * len(self.adj)
        self.processed = list(self.visited)
        self.parent = [None] * len(self.adj)
        self.cc = 0
        self.clock = 0
        self.entry_time = [0] * len(self.adj)
        self.exit_time = list(self.entry_time)
        self.finish = False  # helper variable

    def explore(self, v):
        if self.finish:
            return  # allow early termination

        self.visited[v] = True

        # Tick the entry time
        self.clock += 1
        self.entry_time[v] = self.clock
        self.previsit(v)

        for u in self.adj[v]:
            if not self.visited[u]:
                self.parent[u] = v
                self.process_edge(v, u)  # do something if wanted
                self.explore(u)
            elif self.directed or (not self.processed[u] and self.parent[v] != u):
                # XXX see "The Algorithm Design Manual", section 5.9
                # Processing of back/forward edges
                self.process_edge(v, u)

            if self.finish:
                return  # allow early termination

        self.postvisit(v)
        # Tock the exit time
        self.clock += 1
        self.exit_time[v] = self.clock
        self.processed[v] = True

    def previsit(self, v):
        # Override with whatever you want to do as a pre process of vertex
        pass

    def postvisit(self, v):
        # Override with whatever you want to do as a post process of vertex
        pass

    def process_edge(self, v, u):
        # Override with whatever you want to do when processing an edge
        pass

    def dfs(self):
        for i in range(len(self.adj)):
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


def acyclic(graph):
    is_acyclic = True

    def process_edge(x, y):
        nonlocal is_acyclic
        edge_class = graph.edge_class(x, y)
        # print(x, y, edge_class)
        if edge_class == Graph.BACK_EDGE:  # have cycles, end
            is_acyclic = False
            graph.finish = True  # early termination

    graph.process_edge = process_edge
    graph.dfs()
    return 0 if is_acyclic else 1


if __name__ == '__main__':
    print(acyclic(Graph(sys.stdin.read())))
