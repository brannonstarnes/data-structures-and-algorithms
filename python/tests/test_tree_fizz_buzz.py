from inspect import findsource, formatargvalues
from stack_and_queue.stack_and_queue import Queue
from code_challenges.tree_fizz_buzz.tree_fizz_buzz import K_tree, K_Node, tree_fizz_buzz
import pytest

def test_empty_k_tree():
   tree = K_tree()
   assert tree.root == None

def test_k_tree_returns_root(k_tree):
    assert k_tree.root.value == 1

def test_fizz_buzz(k_tree):
    actual = tree_fizz_buzz(k_tree)
    expected = [1,"Fizz", "Buzz", "FizzBuzz"]
    assert actual == expected


'''
               1
         2         3
     4   5  6    7  8  9
10           12          15'''


@pytest.fixture
def k_tree():
    tree = K_tree(K_Node(1))

    one = K_Node(1)
    two = K_Node(2)
    three = K_Node(3)
    four = K_Node(4)
    five = K_Node(5)
    six = K_Node(6)
    seven= K_Node(7)
    eight = K_Node(8)
    nine = K_Node(9)
    ten = K_Node(10)
    twelve = K_Node(12)
    fifteen = K_Node(15)
    tree.root.children = [K_Node(3),K_Node(5),K_Node(15)]
    return tree


