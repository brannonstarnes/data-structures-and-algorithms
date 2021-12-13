from animal_shelter.stack_queue_animal_shelter import Node, Stack, Animal_Shelter

import pytest

def test_import_Animal_Shelter():
    assert Animal_Shelter

def test_enqueue_dog():
    shelter = Animal_Shelter()
    shelter.enqueue("dog")
    assert shelter._in.peek() == 'dog'

def test_enqueue_dog_cat():
    shelter = Animal_Shelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    assert shelter._in.peek() == 'cat'


def test_dequeue_dog():
    shelter = Animal_Shelter()
    shelter.enqueue('dog')
    shelter.dequeue()
    assert shelter._in.is_empty() == True
