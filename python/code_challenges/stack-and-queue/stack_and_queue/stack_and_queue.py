# typical linked list structure
# class LinkedList:
#     def __init__(self, head):
#         self.head = head


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top = None):
        self.top = top

    def push(self, value):
        self.top = Node(value, self.top)
        if not value:
            raise TypeError("No value to push!")

    def pop(self):
        if self.top is None:
            raise TypeError("Nothing to pop!")
        temp = self.top
        self.top = temp.next

    def peek(self):
        if self.top is None:
            return None
        elif self.top.value:
            return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


class Queue:
    def __init__(self, back = None, front = None):
        self.back= back
        self.front = front

    def enqueue(self, value):
        if self.front is None:
            self.front = Node(value)
            self.back = Node(value)
        elif not self.front is None:
            temp = self.back
            temp.next = value
            self.back = Node(value)

    def dequeue(self):
        if self.front is None:
            raise TypeError("Nothing to dequeue!")
        if self.front.next is None:
            temp = self.front.value
            self.front = None
            self.back = None
            return temp
        if self.front.next:
            print("self.front: ", self.front)
            print("self.front.next: ", self.front.next)
            temp = self.front.value
            self.front = self.front.next
            print("new self.front: ", self.front)
            return temp


    def peek(self):
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
