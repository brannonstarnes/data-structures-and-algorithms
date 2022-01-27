from typing import Type


class Node():
    """
    Node(value, next): Required: "value" to be set as the Node's data. Optional: "next" defaults to None, points to next node in Linked List
    """

    def __init__(self, value, next= None):
        if value == None:
            raise ValueError("Please enter a value.")
        self.value = value
        self.next = next



class LinkedList():
    """Upon instantiation, an empty Linked List should be created, unless a list of values are provided as an argument."""

    def __init__(self, values=None):

        self.head = None

        if values:

            for item in reversed(values):
                self.insert(item)


    def __iter__(self):

        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next

        return value_generator()


    def __len__(self):
        # return len(list(iter(self)))
        count = 0
        for _ in self:
            count += 1
        return count


    def __eq__(self, other):
        return list(self) == list(other)


    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item

        raise IndexError

    def __str__(self):
        """
        Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> None
        """
        output = ""

        for value in self:
            output += f"{{ {value} }} -> "

        return output + 'None'

    def insert(self, value):
        """Adds a new node with provided value to the head of the list with an O(1) Time performance."""
        if value == None:
            raise Exception("Nothing to insert!")

        self.head= Node(value, self.head)



    def insert_before(self, value, new_value):
        """
        .insert_before(value, new_value) -> value is the node in the linked list you will insert the 'new_value' before. 'new_value' is the node value being inserted.
        """

        current_node = self.head
        while current_node:
            if current_node.next.value == value:
                current_node.next = Node(new_value, current_node.next)
                break
            else:
                current_node = current_node.next



    def insert_after(self, value, new_value):
        """
        .insert_after(value, new_value) -> value is the node in the linked list you will insert the 'new_value' after. 'new_value' is the node value being inserted.
        """

        current_node = self.head
        while current_node:
            if current_node.value == value:
                temp = current_node.next
                current_node.next = Node(new_value, temp)
                break
            else:
                current_node = current_node.next


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


    def includes(self, value):
        """.includes(value) - Indicates whether that value exists as a Node’s value somewhere within the list."""

        if self.head == None:
            raise TypeError("Linked List is currently empty.")

        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next

        return False



linked_nums = LinkedList(values=[1,2,3,4,5])
print(linked_nums)
