# Uses python3
import sys
import queue

UNCOLORED, BLACK, WHITE = 0, 1, 2


class Graph:

    def __init__(self, adj_info, directed=False,
                 previsit=lambda self, v: None,
                 postvisit=lambda self, v: None,
                 process_edge=lambda self, u, v: None):
        self.adj = adj_info
        self.directed = directed
        self.initialize()
        self.previsit = previsit
        self.postvisit = postvisit
        self.process_edge = process_edge

    def initialize(self):
        self.visited = [False] * len(self.adj)
        self.distance = [-1] * len(self.adj)
        self.processed = list(self.visited)
        self.parent = [None] * len(self.adj)

    def bfs(self, starting_vertex=0):
        q = queue.Queue()
        self.visited[starting_vertex] = True
        self.distance[starting_vertex] = 0
        q.put(starting_vertex)

        while not q.empty():
            v = q.get()
            self.previsit(self, v)
            self.processed[v] = True

            for u in self.adj[v]:
                if self.directed or not self.processed[u]:
                    self.process_edge(self, v, u)
                if not self.visited[u]:
                    self.parent[u] = v
                    self.visited[u] = True
                    self.distance[u] = self.distance[v] + 1
                    q.put(u)

            self.postvisit(self, v)


def parse_input(input):
    data = list(map(int, input.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return adj


def bipartite(adj):
    color = [UNCOLORED] * len(adj)
    is_bipartite = 1

    def process_edge(self, v, u):
        nonlocal color
        nonlocal is_bipartite
        if color[v] == color[u]:
            is_bipartite = 0
        color[u] = WHITE if color[v] == BLACK else BLACK if color[v] == WHITE else UNCOLORED

    g = Graph(adj, process_edge=process_edge)
    for i in range(len(g.adj)):
        if not g.visited[i]:
            color[i] = WHITE
            g.bfs(i)

    return is_bipartite


if __name__ == '__main__':
    print(bipartite(parse_input(sys.stdin.read())))
