from insertion_sort.insertion_sort import insertion_sort


def test_expected_pass():
    my_list = [4,2,6,44,33]
    assert insertion_sort(my_list) == [2,4,6,33,44]


def test_negatives():
    my_list = [-4,-5,-1,-3]
    assert insertion_sort(my_list) == [-5,-4,-3,-1]

def test_negative_zero_positive():
    my_list = [5,0,-3,4]
    assert insertion_sort(my_list) == [-3,0,4,5]

def test_duplicates():
    my_list = [3,6,2,3]
    assert insertion_sort(my_list) == [2,3,3,6]

def test_one_entry():
    my_list = [2]
    assert insertion_sort(my_list)== [2]

def test_decimals():
    my_list = [1.4, 3.444, 6, 3.555]
    assert insertion_sort(my_list)==[1.4, 3.444, 3.555, 6]

