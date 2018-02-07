# Uses python3
import sys
sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    # write your code here
    return result


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
    print(number_of_strongly_connected_components(parse_input(sys.stdin.read())))
