# Challenge Summary

<!-- Description of the challenge -->

Write a function that takes a given binary tree and returns a list containing each node's value in breadth-first order.

## Whiteboard Process

<!-- Embedded whiteboard image -->

![whiteboard_image](../images/breadth_first.png)

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The breadth_first() function uses a while loop to enqueue and dequeue each node. The queue that is holding the nodes may potentially enqueue at a rate that is twice that of the dequeue rate, therefore, the space requirement will continue to grow as long as there are two child nodes to enqueue.

-   Time - O(n)
-   Space - O(n)

## Solution

Please see the whiteboard above and or click [here]() to view the code.
