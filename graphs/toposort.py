# Uses python3
import sys


def dfs(adj, used, order, x):
    # write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    return order


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
    adj = parse_input(sys.stdin.read())
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
