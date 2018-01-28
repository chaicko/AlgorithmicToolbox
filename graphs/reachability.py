# Uses python3
import sys


def reach(adj, x, y):
    # write your code here
    return 0


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
