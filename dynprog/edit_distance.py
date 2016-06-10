# Uses python3
def edit_distance(s, t):
    # Create matrix 'e' of distances
    z = [0] * len(t)
    ini = [i for i in range(1, len(t) + 1)]
    e = []
    for i in range(len(s) + 1):
        if i == 0:
            e.append([i] + ini)
        else:
            e.append([i] + z)

    # Now compute using algorithm
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insertion, deletion = e[i][j - 1] + 1, e[i - 1][j] + 1
            diff = e[i-1][j-1] if s[i-1] == t[j-1] else e[i-1][j-1] + 1
            e[i][j] = min(insertion, deletion, diff)

    return e[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
