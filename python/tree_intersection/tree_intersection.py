from hash_table.hash_table import HashTable
from binary_tree.binary_tree import BinaryTree

def tree_intersection(tree_1, tree_2):
    # turn tree1 into dictionary,
    tree_a = BinaryTree(tree_1)
    tree_b = BinaryTree(tree_2)


    # if tree2 produces collisions save num to list,
    # if not collision, keep going


    ht = HashTable()
