from linked_list import __version__
import linked_list
from linked_list.linked_list import LinkedList, Node
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_node_value_error():
    with pytest.raises(Exception):
        node = Node()
        node.__init__

def test_node_value_created():
    node = Node('ball')
    assert node.value == 'ball'


def test_node_next():
    node = Node('ball', 'bat')
    assert node.next == 'bat'

def test_node_default_next():
    node = Node('ball')
    assert node.next == None

def test_import_LinkedList():
    assert LinkedList

# Can successfully instantiate an empty linked list

def test_init_empty_linked_list():
    lst = LinkedList()
    actual = lst.head
    expected = None
    assert actual == expected

# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list

def test_insert_node():
    lst = LinkedList()
    lst.insert("ball")
    assert lst.head.value == "ball"

# source: https://docs.pytest.org/en/6.2.x/assert.html

def test_insert_nothing_error():
    with pytest.raises(Exception):
        lst = LinkedList()
        lst.insert()

# Will return false when searching for a value in the linked list that does not exist

def test_includes_return_False():
    lst = LinkedList()
    lst.insert("ball")
    lst.insert("bat")
    assert lst.includes("glove") == False

# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists

def test_includes_return_True(my_list):
    assert my_list.includes("ball") == True


# source: https://docs.pytest.org/en/6.2.x/assert.html

def test_includes_error_empty_list():
    with pytest.raises(TypeError):
        lst = LinkedList()
        lst.includes()



# Can properly return a collection of all the values that exist in the linked list

def test_to_string(my_list):
    assert str(my_list) == "{ glove } -> { ball } -> { bat } -> NULL"


def test_append(my_list):
    my_list.append("hat")
    assert str(my_list) == "{ glove } -> { ball } -> { bat } -> { hat } -> NULL"


def test_append_empty_list():
    lst = LinkedList()
    lst.append("bat")
    assert str(lst) == "{ bat } -> NULL"

def test_append_empty_list():
    lst = LinkedList()
    lst.insert("bat")
    lst.append("ball")
    lst.append("glove")
    assert str(lst) == "{ bat } -> { ball } -> { glove } -> NULL"


def test_insert_before(my_list):
    my_list.insert_before("ball", "hat")
    assert str(my_list) == "{ glove } -> { hat } -> { ball } -> { bat } -> NULL"


def test_insert_after(my_list):
    my_list.insert_after("ball", "hat")
    assert str(my_list) == "{ glove } -> { ball } -> { hat } -> { bat } -> NULL"

def test_kth_from_end_returns_value(my_num_list):
    assert my_num_list.kth_from_end(1) == 10


@pytest.fixture()
def my_list():
    lst = LinkedList()
    lst.insert("bat")
    lst.insert("ball")
    lst.insert("glove")
    return lst

@pytest.fixture()
def my_num_list():
    lst = LinkedList()
    lst.insert(5)
    lst.insert(10)
    lst.insert(15)
    return lst
