# Uses python3
import sys
import queue


class Graph:

    BACK_EDGE, CROSS_EDGE, FORWARD_EDGE, TREE_EDGE = 0, 1, 2, 3

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
        self.initialize()

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


def distance(adj, s, t):
    g = Graph(adj)
    g.bfs(s)
    return g.distance[t]


def parse_input(input):
    data = list(map(int, input.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    return adj, s, t


if __name__ == '__main__':
    print(distance(*parse_input(sys.stdin.read())))
