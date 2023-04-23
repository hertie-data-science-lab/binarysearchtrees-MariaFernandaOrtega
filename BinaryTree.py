# -*- coding: utf-8 -*-
"""

@author: Maria Fernanda Ortega and Maria Jose Lee
"""

from Tree import Tree
from abc import ABC, abstractmethod


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    class Position(ABC):
        """An abstraction representing the location of a single element."""

        @abstractmethod
        def element(self):
            """Return the element stored at this Position."""
            pass

        @abstractmethod
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            pass

        @abstractmethod
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            pass

        @abstractmethod
        def left(self):
            """Return a Position representing the left child of this node.

            Return None if this node does not have a left child.
            """
            pass

        @abstractmethod
        def right(self):
            """Return a Position representing the right child of this node.

            Return None if this node does not have a right child.
            """
            pass

    @abstractmethod
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        pass

    @abstractmethod
    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        pass

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)


