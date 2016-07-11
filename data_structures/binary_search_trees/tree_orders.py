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

    def in_order(self, index, res):
        if index < 0:
            return
        self.in_order(self.left[index], res)
        res.append(self.key[index])
        self.in_order(self.right[index], res)

    def pre_order(self, index, res):
        if index < 0:
            return
        res.append(self.key[index])
        self.pre_order(self.left[index], res)
        self.pre_order(self.right[index], res)

    def post_order(self, index, res):
        if index < 0:
            return
        self.post_order(self.left[index], res)
        self.post_order(self.right[index], res)
        res.append(self.key[index])

    @staticmethod
    def order(method):
        result = []
        method(0, result)
        return result


if __name__ == "__main__":
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
        print(" ".join(str(x) for x in tree.order(tree.in_order)))
        print(" ".join(str(x) for x in tree.order(tree.pre_order)))
        print(" ".join(str(x) for x in tree.order(tree.post_order)))

    threading.Thread(target=main).start()
