# python3

from sys import stdin


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (
        key, sum, left, right, parent)


def update(v):
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent is not None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent is not None:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v is not None:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result is None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left is not None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left is not None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    (result, root) = find(root, x)
    if result and result.key == x:
        (left, middle) = split(root, x)
        (middle, right) = split(middle, x + 1)
        root = merge(left, right)
        del middle


def search(x):
    global root
    (result, root) = find(root, x)
    return result and result.key == x


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = middle.sum if middle else 0
    # Complete the implementation of sum
    # print("Contents:")
    # if left:
    #     print("Left", left.key, left.sum)
    # if middle:
    #     print("middle", middle.key, middle.sum)
    # if right:
    #     print("Right", right.key, right.sum)

    root = merge(merge(left, middle), right)

    return ans

MODULO = 1000000001


class RangeSumProcessor:
    def __init__(self):
        self.last_sum_result = 0

    def process(self, cmd):
        ret = None
        _cmd = cmd.split()
        if _cmd[0] == '+':
            x = int(_cmd[1])
            insert((x + self.last_sum_result) % MODULO)
        elif _cmd[0] == '-':
            x = int(_cmd[1])
            erase((x + self.last_sum_result) % MODULO)
        elif _cmd[0] == '?':
            x = int(_cmd[1])
            if search((x + self.last_sum_result) % MODULO):
                ret = 'Found'
            else:
                ret = 'Not found'
        elif _cmd[0] == 's':
            l = int(_cmd[1])
            r = int(_cmd[2])
            res = sum((l + self.last_sum_result) % MODULO,
                      (r + self.last_sum_result) % MODULO)
            ret = str(res)
            self.last_sum_result = res % MODULO
        return ret


if __name__ == "__main__":
    processor = RangeSumProcessor()
    n = int(stdin.readline())
    for i in range(n):
        line = stdin.readline()
        res = processor.process(line)
        if res:
            print(res)
