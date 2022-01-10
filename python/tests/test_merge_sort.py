from merge_sort.merge_sort import *
import pytest

@pytest.mark.skip("finish code")
def test_expected():
    my_list = [3,4,2,1]
    assert merge_sort(my_list) == [1,2,3,4]
@pytest.mark.skip("finish code")
def test_uneven():
    my_list = [4,2,3]
    assert merge_sort(my_list) == [2,3,4]
@pytest.mark.skip("finish code")
def test_negatives():
    my_list = [-1,3,-4,4]
    assert merge_sort(my_list) == [-4,-1,3,4]
@pytest.mark.skip("finish code")
def test_decimals():
    my_list = [.3 , 2.5, 1.2, 2.3]
    assert merge_sort(my_list) == [.3, 1.2, 2.3, 2.5]
