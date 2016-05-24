# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    c = sorted(zip(weights, values), key=lambda item: item[1] / item[0])
    value = 0.
    while 0 < capacity and len(c):
        wi, vi = c.pop()  # get item with highest (value / weight) value
        xi = 1.0
        if wi > capacity:
            xi = capacity / wi
        capacity -= wi
        value += xi * vi

    return value


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


if __name__ == "__main__":
    main()
