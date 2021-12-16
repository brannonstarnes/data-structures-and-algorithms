from   import deque
acceptable_animals = ['dog', 'cat']

class Dog():
    pass

class Cat():
    pass


class Animal_Shelter:
    def __init__(self):
        self._cats = Queue()    # creates a cat queue
        self._dogs = Queue()    # creates a dog queue

    def enqueue(self, animal):
        if isinstance(self, animal):
            self._cats.enqueue(animal) 
        else:
            self._dogs.enqueue(animal)

    def dequeue(self, pref):
        if pref == 'cat':
            return self._cats.dequeue()
        else:
            return None


class Dog:
    pass

class Cat:
    pass
