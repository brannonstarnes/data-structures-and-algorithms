from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node

class BinarySearchTree(BinaryTree):

    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        def walk(root):
          if new_node.value < root.value:
              if root.left is None:
                  root.left = new_node
                  return
              walk(root.left)
          if new_node.value > root.value:
              if root.right is None:
                  root.right = new_node
                  return
              walk(root.right)
        walk(self.root)


    def contains(self, value):
        result = self.in_order()
        if value in result:
            return True
        else:
            return False


# Create a Binary Search Tree class
# This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
# Add
# Arguments: value
# Return: nothing
# Adds a new node with that value in the correct location in the binary search tree.
# Contains
# Argument: value
# Returns: boolean indicating whether or not the value is in the tree at least once.
