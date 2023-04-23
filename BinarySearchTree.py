"""

@author: Maria Fernanda Ortega and Maria Jose Lee
"""
from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):


    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, left=None, right=None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def parent(self, p):
        return None

    def left(self, p):
        return p._left

    def right(self, p):
        return p._right

    def num_children(self, p):
        count = 0
        if p._left is not None:
            count += 1
        if p._right is not None:
            count += 1
        return count

    def inorder_traversal(self):

        if self._root is not None:
            yield from self._inorder_traversal(self._root)

    def _inorder_traversal(self, p):

        if p._left is not None:
            yield from self._inorder_traversal(p._left)
        yield p._element
        if p._right is not None:
            yield from self._inorder_traversal(p._right)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self._Node(e)
        self._size = 1
        return self._root

    def add_left(self, p, e):
        if p._left is not None:
            raise ValueError('Left child exists')
        p._left = self._Node(e)
        self._size += 1
        return p._left

    def add_right(self, p, e):
        if p._right is not None:
            raise ValueError('Right child exists')
        p._right = self._Node(e)
        self._size += 1
        return p._right

def binary_tree_to_bst(tree):

    nodes = []
    for node in tree.inorder_traversal():
        nodes.append(node)
    nodes.sort()
    return _binary_tree_to_bst_helper(nodes, 0, len(nodes) - 1)

def _binary_tree_to_bst_helper(nodes, start, end):

    if start > end:
        return None
    mid = (start + end) // 2
    root = BinarySearchTree._Node(nodes[mid])
    root._left = _binary_tree_to_bst_helper(nodes, start, mid - 1)
    root._right = _binary_tree_to_bst_helper(nodes, mid + 1, end)
    return root

