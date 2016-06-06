# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


MAX_OPERANDS = 14 * 2
MAX_INPUT = MAX_OPERANDS + 1
MAX_VALUE = 9 ** MAX_OPERANDS  # 28 nines multiplied to each other


def get_maximum_value(dataset):
    # get operands and operators
    operands = []
    operators = []
    for i, c in enumerate(dataset):
        if i % 2:
            operators.append(c)
        else:
            operands.append(int(c))

    # Initialize Matrices
    n = len(operands)
    m = []
    M = []
    for i in range(n):
        m.append([operands[j] if j == i else 0 for j in range(n)])
        M.append([operands[j] if j == i else 0 for j in range(n)])

    # inner function to compute min_and_max
    def min_and_max(i, j):
        min_ = MAX_VALUE
        max_ = -MAX_VALUE
        for k in range(i, j):
            a = evalt(M[i][k], M[k + 1][j], operators[k])
            b = evalt(M[i][k], m[k + 1][j], operators[k])
            c = evalt(m[i][k], M[k + 1][j], operators[k])
            d = evalt(m[i][k], m[k + 1][j], operators[k])
            min_ = min(a, b, c, d, min_)
            max_ = max(a, b, c, d, max_)
        return min_, max_

    # main compute loop, from slides
    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            # have to fix the indexes
            m[i - 1][j - 1], M[i - 1][j - 1] = min_and_max(i - 1, j - 1)

    return M[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
