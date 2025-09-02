# TODO: 사용자 모듈 import
from basic_funcs import check_even_odd, get_avg, get_max, get_min


# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
def test_even_odd():
    assert check_even_odd(-2) is True
    assert check_even_odd(-1) is False
    assert check_even_odd(0) is True
    assert check_even_odd(1) is False
    assert check_even_odd(2) is True

def test_avg():
    assert get_avg([]) is None
    assert get_avg([-1, 1]) == 0
    assert get_avg([1, 2, 3, 4, 5, 6]) == 3.5

def test_max():
    assert get_max([]) is None
    assert get_max([-1, 1]) == 1
    assert get_max([2, 1, 4, 6, 5, 3]) == 6

def test_min():
    assert get_min([]) is None
    assert get_min([-1, 1]) == -1
    assert get_min([2, 1, 4, 6, 5, 3]) == 1
