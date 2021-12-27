from code_challenges import linked_list_zip
from code_challenges.linked_list_zip.linked_list_zip import zip_lists, LinkedList, Node
import pytest


def test_zip_expected_outcome():
    list1 = LinkedList()
    list1.insert("C")
    list1.insert("B")
    list1.insert("A")

    list2 = LinkedList()
    list2.insert("3")
    list2.insert("2")
    list2.insert("1")

    zipped = zip_lists(list1, list2)

    assert (zipped.head.value, zipped.head.next.value, zipped.head.next.next.value, zipped.head.next.next.next.value, zipped.head.next.next.next.next.value, zipped.head.next.next.next.next.next.value) == ("A", "1","B", "2", "C", "3")

def test_one_empty_list_raises_exception():

    list1 = LinkedList()
    list1.insert("C")
    list1.insert("B")
    list1.insert("A")

    list2 = LinkedList()

    with pytest.raises(Exception):
        zipped = zip_lists(list1, list2)

def test_differing_lengths():
    list1 = LinkedList()
    list1.insert("C")
    list1.insert("B")
    list1.insert("A")

    list2 = LinkedList()
    list2.insert("1")

    zipped = zip_lists(list1, list2)

    assert (zipped.head.value, zipped.head.next.value, zipped.head.next.next.value, zipped.head.next.next.next.value) == ("A", "1","B", "C")
