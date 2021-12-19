# Trees

<!-- Short summary or background information -->

Binary and K-ary trees are Node-centric data structures that have a root a a possible number of children (k).

## Challenge

<!-- Description of the challenge -->

Create a binary_tree class and binary_search_tree subclass and their methods. Include a method to add a node to the appropriate location in the tree, a method to search whether a value is contained in the tree, and methods to return the order in which the tree is searched (ie. pre-order, in-order, and post-order).

## Approach & Efficiency

BigO for Time is O(logN). Binary search methods cut the search pool in half each iteration.
BigO for Space is O(n), since space required is directly related to the size of the tree.

## API

<!-- Description of each method publicly available in each of your trees -->

-   .add(value) - takes a given value, adds it as a Node object to the appropriate location in the tree.
-   .contains(value) - takes a given value and searches the tree for a Node whose value is equal to the given value. Returns a boolean.

Each method below returns a list of Nodes following the an ordered search pattern:

-   .pre_order() - root >> left-child >> right-child
-   .in_order() - left-child >> root >> right-child
-   .post_order() - left-child >> right_child >> root
