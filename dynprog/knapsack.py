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
            K[x][j] = K[x][j - 1]  # for a bag of weight x we use j-1 items
            if wj <= x:  # if item weight is at most the current knapsack
                # compute the value we get if using item j, for knapsack x
                val = K[x - wj][j - 1] + vj
                if K[x][j] < val:  # if value is greater when using it
                    K[x][j] = val  # use it

    return K[W][n]


def main():
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


if __name__ == '__main__':
    main()
