from stack_queue_brackets.stack_queue_brackets import validate_brackets
from stack_and_queue.stack_and_queue import Stack
import pytest

def test_validate_balanced():
    string = "[]"
    assert validate_brackets(string) == True
def test_validate_more_balanced():
    string = "[()]"
    assert validate_brackets(string) == True
def test_validate__even_more_balanced():
    string = "[{()}]"
    assert validate_brackets(string) == True
def test_validate_unbalanced():
    string = "[}"
    assert validate_brackets(string) == False
def test_validate_offbalance():
    string = "[()"
    assert validate_brackets(string) == False
