class Dog:
    def __init__(self, name, next= None):
        self.name = name
        self.next = next

class Cat():
    def __init__(self, name, next= None):
        self.name = name
        self.next = next

class Queue:
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, animal):
        if self.front is None:
            self.front = animal
            self.back = self.front
        elif self.front:
            temp = self.back
            temp.next = animal
            self.back = temp.next

    def is_empty(self):
            if self.front is None:
                return True
            else:
                return False

class Animal_Shelter():
    def __init__(self):
        self._cats = Queue()    # creates a cat queue
        self._dogs = Queue()    # creates a dog queue


    def dequeue(self, pref):
            if pref == 'cat':
                preferred_queue = self._cats
            elif pref == 'dog':
                preferred_queue = self._dogs
            else:
                return None

            if preferred_queue.is_empty():
                raise TypeError("Nothing to dequeue!")
            if preferred_queue.front.next is None:
                temp = preferred_queue.front.value
                preferred_queue.front = None
                preferred_queue.back = None
                return temp
            elif preferred_queue.front.next:
                temp = preferred_queue.front
                preferred_queue.front = preferred_queue.front.next
                return temp.name
