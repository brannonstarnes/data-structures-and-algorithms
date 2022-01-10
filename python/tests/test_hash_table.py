import pytest
from hash_table.hash_table import HashTable

def test_hash_created():
    my_hash = HashTable()
    actual = my_hash.hash("spam")
    expected = 295
    assert actual == expected

def test_get_return_true():
    pass
