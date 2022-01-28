from decorators.decorators import func_duration

@func_duration
def make_list(int):
    result = []
    for i in range(1,int+1):
        result.append(i)
    return


def test_return_float():
    actual = make_list(10)
    assert type(actual) is float


def test_higher_load_returns_higher_duration_value():
    lower = make_list(2)
    higher = make_list(2000000) #number must be sufficiently high enough to rule out machine speed fluctuations
    assert lower < higher


