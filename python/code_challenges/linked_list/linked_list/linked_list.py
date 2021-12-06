# DONE Create a Linked List class
# DONE Within your Linked List class, include a head property.

from typing import Type


class Node():
    """
    Node(value, next): Required: "value" to be set as the Node's data. Optional: "next" defaults to None, points to next node in Linked List """

    def __init__(self, value, next= None):
        if value == None:
            raise ValueError("Please enter a value.")
        self.value = value
        self.next = next


# DONE Upon instantiation, an empty Linked List should be created.
class LinkedList():
    def __init__(self):
        self.head = None


# DONE insert
# Arguments: value
# Returns: nothing
# Adds a new node with that value to the head of the list with an O(1) Time performance.
    def insert(self, value):

        if value == None:
            raise Exception("Nothing to insert!")

        self.head= Node(value, self.head)



# DONE includes
# Arguments: value
# Returns: Boolean
# Indicates whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):

        if self.head == None:
            raise TypeError("Linked List is currently empty.")

        current_Node = self.head
        while current_Node:
            if current_Node.value == value:
                return True
            else:
                current_Node = current_Node.next

        return False


# DONE to string
# Arguments: none
# Returns: a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
    def __str__(self):

        current_Node = self.head
        lst_string = ""

        while current_Node:
            lst_string += "{ " + current_Node.value + " } -> "
            current_Node = current_Node.next
        lst_string += "NULL"

        return lst_string

