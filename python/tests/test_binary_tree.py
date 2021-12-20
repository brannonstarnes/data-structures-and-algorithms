from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node
from binary_tree.binary_search_tree import BinarySearchTree
import pytest

# DONE Can successfully instantiate an empty tree
def test_empty_binary_tree():
    empty_tree = BinaryTree()
    assert empty_tree.root == None

# DONE Can successfully instantiate a tree with a single root node
def test_single_node_tree():
    tree = BinaryTree(Node("spam"))
    assert tree.root.value == 'spam'
    assert tree.root.left == None
    assert tree.root.right == None

#  Can successfully add a left child and right child to a single root node
def test_left_right_child():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.left.value == 5 and tree.root.right.value == 15


def test_single_node_add():
    tree= BinarySearchTree()
    tree.add(1)
    assert tree.root.value == 1

# DONE Can successfully return a collection from a preorder traversal
def test_preorder_collection(bal_tree):
    assert bal_tree.pre_order() == [10,5,2,7,15,12,20]

# DONE Can successfully return a collection from an inorder traversal
def test_inorder_collection(bal_tree):
    assert bal_tree.in_order() == [2,5,7,10,12,15,20]

# DONE Can successfully return a collection from a postorder traversal
def test_postorder_collection(bal_tree):
    assert bal_tree.post_order() == [2,7,5,12,20,15,10]

def test_unbalanced_tree_preorder(unbal_tree):
    assert unbal_tree.pre_order() == [10,5,2,7,15]

def test_single_node_inorder():
    tree= BinarySearchTree()
    tree.add(4)
    assert tree.in_order() == [4]

def test_contains_value_true(bal_tree):
    assert bal_tree.contains(5) == True

def test_contains_value_false(bal_tree):
    assert bal_tree.contains(50) == False

def test_max_root_two_children(bin_tree):
    assert bin_tree.find_max() == 10




@pytest.fixture
def bal_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(15)
    tree.add(12)
    tree.add(20)
    return tree

@pytest.fixture
def unbal_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(15)
    return tree

@pytest.fixture
def bin_tree():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(6)
    tree.root.right = Node(10)
    return tree
