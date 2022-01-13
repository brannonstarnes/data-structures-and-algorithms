import pytest
from hash_table.hash_table import HashTable

@pytest.mark.skip('refactor')
def test_hash_created():
    my_hash = HashTable()
    actual = my_hash.hash("spam")
    expected = 295
    assert actual == expected

@pytest.mark.skip('refactor')
def test_collision_hash():
    my_hash = HashTable()
    actual = my_hash.hash("maps")
    expected = 295
    assert actual == expected

@pytest.mark.skip('refactor')
def test_get_return_expected():
    my_hash = HashTable()
    my_hash.add('spam', 'eggs')
    actual = my_hash.get('spam')
    eggspected = 'eggs'
    assert actual == eggspected

@pytest.mark.skip('refactor')
def test_add_collision():
    pass

# my_hash.contains('spam')
# my_hash.contains('foo')
