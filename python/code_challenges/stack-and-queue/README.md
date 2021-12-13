# Stacks and Queues

Stacks and Queues represent an evolution of Linked Lists. Their nodes may be added, removed, or otherwise accessed differently from that of a traditional linked list. Stacks can be thought of as stacks of pancakes, where only the top node can be accessed. Queues have a "front of the line" and a "back of the line". The front may be removed, but all new nodes are added to the back of the line.

## Challenge

Create classes for Stack and Queue structures to store nodes and write methods:

## Approach & Efficiency

    Approach was to keep Big O time to O(1). Space is O(n) dependent on Stack/Queue length.

## API

-   Stack:
    -   push() - adds node to top of stack
    -   pop() - removes top node from stack
    -   peek() - returns top node value
    -   is_empty() - returns Boolean if Stack is/is not empty
-   Queue:
    -   enqueue() - adds node to back of queue
    -   dequeue() - removes node from front of queue, returns its value
    -   peek() - returns front node's value
    -   is_empty() - returns Boolean if Queue is/is not empty
