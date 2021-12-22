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
            self.back = self.front
        elif self.front:
            temp = self.back
            temp.next = Node(value)
            self.back = temp.next

    def dequeue(self):
        if self.is_empty():
            raise TypeError("Nothing to dequeue!")
        if self.front.next is None:
            temp = self.front.value
            self.front = None
            self.back = None
            return temp
        elif self.front.next:
            temp = self.front
            self.front = self.front.next
            return temp.value


    def peek(self):
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class PseudoQueue:
    def __init__(self, _in = None, _out = None):
        self._in = Stack(_in)
        self._out = Stack(_out)

    def enqueue(self, value):
        if self._in.peek() is None and self._out.peek() is None:
            self._in.push(value)

        elif self._out.peek():
            text = ""
            while self._out.peek():
                if self._out.peek():
                    text += f"[{self._out.peek()}]->"
                    self._in.push(self._out.pop())
            self._in.push(value)
            text += f"[{value}]->None"
            print(text)
            return text
        elif not self._out.peek() and self._in.peek():
            self._in.push(value)

    def dequeue(self):
        if not self._in.peek() and not self._out.peek():
            raise TypeError("Nothing to dequeue!")
        elif self._in.peek():
            while self._in.peek():
                self._out.push(self._in.pop())
            return self._out.pop()

        elif self._out.peek():
            return self._out.pop()

