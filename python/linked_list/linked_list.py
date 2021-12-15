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



    def insert_before(self, value, new_value):
        """
        .insert_before(value, new_value) -> value is the node in the linked list you will insert the 'new_value' before. 'new_value' is the node value being inserted."""

        current_node = self.head
        while current_node:
            if current_node.next.value == value:
                current_node.next = Node(new_value, current_node.next)
                break
            else:
                current_node = current_node.next



    def insert_after(self, value, new_value):
        """
        .insert_after(value, new_value) -> value is the node in the linked list you will insert the 'new_value' after. 'new_value' is the node value being inserted."""

        current_node = self.head
        while current_node:
            if current_node.value == value:
                temp = current_node.next
                current_node.next = Node(new_value, temp)
                break
            else:
                current_node = current_node.next




# Challenge 06 DONE
    def append(self, value):

        if self.head == None:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node:
            if current_node.next == None:
                current_node.next = Node(value)
                break
            else:
                current_node = current_node.next


# DONE includes
# Arguments: value
# Returns: Boolean
# Indicates whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):

        if self.head == None:
            raise TypeError("Linked List is currently empty.")

        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next

        return False


# DONE to string
# Arguments: none
# Returns: a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
    def __str__(self):

        current_node = self.head
        lst_string = ""

        while current_node:
            lst_string += "{ " + current_node.value + " } -> "
            current_node = current_node.next
        lst_string += "NULL"

        return lst_string

