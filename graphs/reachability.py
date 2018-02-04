# Uses python3
import sys

MIN_VERTICES, MAX_VERTICES = (2, 10**3)
MIN_EDGES, MAX_EDGES = (1, 10**3)


def explore(adj, x):
    visited = [False] * len(adj)

    def _explore(v):
        nonlocal visited  # reference to outer scope visited
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                _explore(u)
    _explore(x)

    return visited


def reach(adj, x, y):
    if adj[x] == []:
        return 0  # Non reachable
    elif y in adj[x]:  # immediate neighbour
        return 1
    visited = explore(adj, x)
    return 1 if visited[y] else 0


def parse_input(input):
    data = list(map(int, input.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    x, y = data[2 * m:]
    x, y = x - 1, y - 1

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    return adj, x, y


if __name__ == '__main__':
    print(reach(*parse_input(sys.stdin.read())))
