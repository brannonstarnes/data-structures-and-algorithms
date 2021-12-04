# Singly Linked List

<!-- Short summary or background information -->

In a linked list, a Node will contain data and a reference to the "next" node in the list. The last node in the list containing a value will point next to "None". Testing can be found in tests/test_linked_list.py

## Challenge

<!-- Description of the challenge -->

Create and a linked list class and node class and write their methods, properties, and tests.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The approach was to keep the class properties, and tests clearly written and easy to decipher. Red, green, refactor method used on testing.

#### BigO

-   Time: O(n) for methods such as "includes()"
-   Space: O(n), as the list increases, memory will follow.

## API

<!-- Description of each method publicly available to your Linked List -->

### Node()

-   \_\_init\_\_ creates a Node instance

### LinkedList()

-   .\_\_init\_\_ creates a Linked List instance

-   .insert - takes in a Node, adds a new node to the linked list head position and sets previous 'head' to 'next'

-   .includes - takes a value, searches each node in the linked list for the value, returns a Boolean.

-   .\_\_str\_\_ - takes in a linked list instance, returns all nodes as a string in the form: " {a} -> {b} -> {c} -> NULL"
