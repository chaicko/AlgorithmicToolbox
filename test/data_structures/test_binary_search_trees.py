# import data_structures.binary_search_trees.rope as rope
# import data_structures.binary_search_trees.set_range_sum as set_range_sum
import data_structures.binary_search_trees.tree_orders as tree_orders

import pytest
import os
import sys
import resource

CI = os.environ.get('CI') == 'true'


# Helpers
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def get(self, key):
        if self.root:
            res = self.find(key, self.root)
            if res and res.key == key:
                return res.payload
            else:
                return None
        else:
            return None

    def find(self, key, node):
        if node.key == key:
            return node

        if key < node.key:
            if not node.has_left_child():
                return node
            return self.find(key, node.left_child)
        else:
            if not node.has_right_child():
                return node
            return self.find(key, node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def put(self, key, val):
        if self.root:
            print("put on empty")
            self._put(key, val, self.root)
        else:
            print("put on non empty")
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, node):
        _parent = self.find(key, node)
        if _parent.key == key:  # already exists, replace values
            _parent.replace_node_data(key, val, _parent.left_child,
                                      _parent.right_child)
            return

        # At this point is guaranteed that _parent has null child
        if key < _parent.key:
            assert not _parent.has_left_child()
            _parent.left_child = TreeNode(key, val, parent=_parent)
        else:
            assert not _parent.has_right_child()
            _parent.right_child = TreeNode(key, val, parent=_parent)

    def __setitem__(self, k, v):
        """
        Allows usage of [].
        :param k:
        :param v:
        :return:
        """
        self.put(k, v)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


@pytest.mark.timeout(6)
class TestTreeOrders:
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        sys.setrecursionlimit(10 ** 6)  # max depth of recursion
        resource.setrlimit(resource.RLIMIT_STACK, (2 ** 27, 2 ** 27))

    @pytest.mark.parametrize("n,key,left,right,exp_inorder,exp_preorder,exp_postorder", [
        (5,
         [4, 2, 5, 1, 3],
         [1, 3, -1, -1, -1],
         [2, 4, -1, -1, -1],
         [1, 2, 3, 4, 5], [4, 2, 1, 3, 5], [1, 3, 2, 5, 4]),
        (10,
         [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
         [7, -1, -1, 8, 3, -1, 1, 5, -1, -1],
         [2, -1, 6, 9, -1, -1, -1, 4, -1, -1],
         [50, 70, 80, 30, 90, 40, 0, 20, 10, 60],
         [0, 70, 50, 40, 30, 80, 90, 20, 60, 10],
         [50, 80, 90, 30, 40, 70, 10, 60, 20, 0])
    ])
    def test_samples(self, n,key,left,right,exp_inorder,exp_preorder,exp_postorder):
        tree = tree_orders.TreeOrders(n, key, left, right)
        assert exp_inorder == tree.order(tree.in_order)
        assert exp_preorder == tree.order(tree.pre_order)
        assert exp_postorder == tree.order(tree.post_order)

