# Uses python3
import sys

MIN_VERTICES, MAX_VERTICES = (2, 10**3)
MIN_EDGES, MAX_EDGES = (1, 10**3)


def explore(adj, x, visited):

    def _explore(v):
        nonlocal visited  # reference to outer scope visited
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                _explore(u)
    _explore(x)


def number_of_components(adj):
    visited = [False] * len(adj)
    cc = 0
    for i in range(len(adj)):
        if not visited[i]:
            explore(adj, i, visited)
            cc += 1
    return cc


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


if __name__ == '__main__':
    print(number_of_components(parse_input(sys.stdin.read())))