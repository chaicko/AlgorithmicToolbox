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


def toposort(graph):
    order = list()

    def push_vertex(g, v):
        order.append(v)

    graph.postvisit = push_vertex
    graph.dfs()  # do the DFS
    return reversed(order)


def toposort_str(adj_info_str, directed=True):
    graph = Graph(adj_info_str, directed=directed)
    return " ".join(str(i+1) for i in toposort(graph))


if __name__ == '__main__':
    print(toposort_str(sys.stdin.read(), directed=True))
