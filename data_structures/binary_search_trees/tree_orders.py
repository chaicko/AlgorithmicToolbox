# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self, n, key, left, right):
        self.n = n
        self.key = key
        self.left = left
        self.right = right

    def in_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def pre_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def post_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
    n = int(sys.stdin.readline())
    key = [0] * n
    left = list(key)
    right = list(key)
    for i in range(n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        key[i] = a
        left[i] = b
        right[i] = c

    tree = TreeOrders(n, key, left, right)
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


if __name__ == "__main__":
    threading.Thread(target=main).start()
