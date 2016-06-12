# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeHeight:
    def __init__(self, size=0, parent=[]):
        self.n = size
        self.parent = parent
        self.tree = {}

    def build_tree(self):
        """
        This method creates a dictionary whose keys
        are the index of a subtree and whose values are lists of the
        childs for the given subtree. The root of the whole tree has key -1.
        For example:
        {
            -1: [1],
            1: [3, 4]
            4: [0, 2]
        }
        Is the following tree:
                [1]
            [3]    [4]
                 [0] [2]
        """
        for i, n in enumerate(self.parent):
            if n not in self.tree:
                self.tree[n] = []

            self.tree[n] += [i]  # append index

    def height(self, key):
        """
        Computes the height of a given subtree with root 'key'.
        :param key:
        :return:
        """
        if key not in self.tree:
            return 0

        mx = 0
        for k in self.tree[key]:
            # We have to compute the height of all child subtrees and pick the
            # one with max depth
            mx = max(mx, self.height(k))
        return 1 + mx

    def compute_height(self):
        self.build_tree()
        max_height = self.height(-1)  # compute height starting from root
        return max_height


def main():
    n = int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    tree = TreeHeight(n, parent)
    print(tree.compute_height())


if __name__ == "__main__":
    threading.Thread(target=main).start()
