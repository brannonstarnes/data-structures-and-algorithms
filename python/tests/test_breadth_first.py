from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node
import pytest

def test_one_root(small_tree):
    assert breadth_first(small_tree) == [1,2,3]

def test_big_tree_and_None_as_value(big_tree):
    assert breadth_first(big_tree) == [2,7,5,2,6,9,None,11,4]

def test_empty_tree():
    with pytest.raises(ValueError):
        empty_tree = BinaryTree()
        breadth_first(empty_tree)

@pytest.fixture
def small_tree():
    tree = BinaryTree()
    tree.root = Node(1,2,3)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    return tree

@pytest.fixture
def big_tree():
    tree = BinaryTree()
    tree.root = Node(2,7,5)
    tree.root.left = Node(7,2,6)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6,5,11)
    tree.root.left.right.left = Node(None)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(5)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree
