# Uses python3
import sys


def optimal_weight(W, w):
    n = len(w)
    # Initialize matrix K
    z = [0] * (n + 1)
    K = []
    for i in range(W + 1):
        K.append(list(z))

    # Execute the algorithm as in the slides/book
    for j in range(1, n + 1):
        wj = w[j - 1]
        vj = wj  # lets take the value to be the same as the weight
        for x in range(1, W + 1):
            if wj > x:  # if item weight is more than current knapsack x
                # Then we do not use it
                K[x][j] = K[x][j - 1]
            else:  # we might use if its value is higher
                K[x][j] = max(K[x][j - 1], K[x - wj][j - 1] + vj)

    return K[W][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
