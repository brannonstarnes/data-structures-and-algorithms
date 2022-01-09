from quick_sort.quick_sort import *
import pytest

def test_expected():
    my_list = [3,2,5,1]
    assert quick_sort(my_list) == [1,2,3,5]
