# Singly Linked List

<!-- Short summary or background information -->

Singly Linked Lists consist of nodes that contain their own value a reference value that points to the next node in the list.

## Challenge

<!-- Description of the challenge -->

Create a Node class and Linked List class each with appropriate methods for building and editing a Linked List.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

.insert is an O(1) method that maintains simplicity and high efficiency. .includes and .to_string are dependent on length of the list so is O(n).

## API

-   .append() - takes in a value and places a node with that value at the end of the linked list.

-   .insert() - takes in a value and places a node containing that value as the head of the linked list.

-   .insert_before() - takes in two values (existing_value, new_value) and places a node with the new value before the node with the existing value in the linked list.

-   .insert_after() - takes in two values (existing_value, new_value) and places a node with the new value after the node with the existing value in the linked list.

-   .includes() - takes in a value and checks the linked list for that value. Returns a boolean.

-   .to_string() - method that returns a string representation of the linked list such as :
    "{a} -> {b} -> {c} -> None"
