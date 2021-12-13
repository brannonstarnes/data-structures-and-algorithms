acceptable_animals = ['dog', 'cat']

class Node:
    def __init__(self, animal, next = None):
        self.animal = animal
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
        elif self.top.animal:
            return self.top.animal

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


class Animal_Shelter:
    def __init__(self, _in = None, _out = None):
        self._in = Stack(_in)
        self._out = Stack(_out)

    def enqueue(self, animal):
        if animal in acceptable_animals:
            if self._in.peek() is None and self._out.peek() is None:
                self._in.push(animal)

            elif self._out.peek():
                text = ""
                while self._out.peek():
                    if self._out.peek():
                        text += f"[{self._out.peek()}]->"
                        self._in.push(self._out.pop())
                self._in.push(animal)
                text += f"[{animal}]->None"
                print(text)
                return text
            elif not self._out.peek() and self._in.peek():
                self._in.push(animal)
        else:
            return "Shelter can only take a cat or dog."

    def dequeue(self):
        if self._in.is_empty() and self._out.is_empty():
            raise TypeError("Nothing to dequeue!")
        elif not self._in.is_empty():
            while not self._in.is_empty():
                self._out.push(self._in.pop())
            return self._out.pop()

        elif not self._out.is_empty():
            return self._out.pop()

