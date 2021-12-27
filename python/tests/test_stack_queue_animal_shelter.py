from animal_shelter.stack_queue_animal_shelter import Animal_Shelter, Queue, Dog, Cat
import pytest

def test_add_dogs():
    shelter = Animal_Shelter()
    shelter._dogs.enqueue(Dog("Sparky"))
    shelter._dogs.enqueue(Dog("Jojo"))
    assert shelter._dogs.front.name == "Sparky"
    assert shelter._dogs.back.name == "Jojo"

def test_add_cats():
    shelter = Animal_Shelter()
    shelter._cats.enqueue(Cat("Mittens"))
    shelter._cats.enqueue(Cat("Socks"))
    assert shelter._cats.front.name == "Mittens"
    assert shelter._cats.back.name == "Socks"

def test_dequeue_cats():
    shelter = Animal_Shelter()
    shelter._cats.enqueue(Cat("Mittens"))
    shelter._cats.enqueue(Cat("Socks"))
    shelter.dequeue('cat')
    assert shelter._cats.front.name == "Socks"
    assert shelter._cats.back.name == "Socks"

def test_dequeue_dogs():
    shelter = Animal_Shelter()
    shelter._dogs.enqueue(Dog("Sparky"))
    shelter._dogs.enqueue(Dog("Jojo"))
    shelter.dequeue('dog')
    assert shelter._dogs.front.name == "Jojo"
    assert shelter._dogs.back.name == "Jojo"

def test_lizard_return_none():
    shelter = Animal_Shelter()
    shelter._dogs.enqueue(Dog("Sparky"))
    shelter._cats.enqueue(Cat("Mittens"))
    actual = shelter.dequeue('lizard')
    expected = None
    assert actual == expected
