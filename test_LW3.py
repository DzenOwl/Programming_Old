import pytest
import math
# height
def check_height(height) -> float:
    try:
        height = float(height)
    except (TypeError, ValueError):
        raise ValueError('Incorrect value. Write the right answer, please')
    if height <= 0:
        raise ValueError('Incorrect value. The capacity must be a number >= 0')
    return height

def test_check_check_height():
    assert check_height(5) == 5
    assert check_height(2.3) == 2.3

def test_check_check_height_errors():
    with pytest.raises(ValueError):
        check_height("qwerty")
    with pytest.raises(ValueError):
        check_height(0)

# num
def check_num(num) -> int:
    if type(num) is not in [str, int]:
        raise TypeError('Incorrect value. The capacity must be an integer number >=0')
    try:
        num = int(num)
    except ValueError:
        raise ValueError('Incorrect value. Write the right answer, please')
    if num <= 0:
        raise ValueError('Incorrect value. The capacity must be an integer number >= 0')
    return num


def test_check_num():
    assert check_num("5") == 5
    assert check_num("2") == 2

def test_check_num_errors():
    with pytest.raises(ValueError):
        check_num("qwerty")
    with pytest.raises(ValueError):
        check_num(0)
    with pytest.raises(TypeError):
        check_num(2.3)

# all heights
def all_heights(height, num):
    # Syntax sugar:
    H = height
    N = num
    all_heights = []

    for i in range(1, N):
        all_heights.append(round(math.sqrt(i) * H / math.sqrt(N), 2))
    return all_heights


def test_all_heights():
    assert all_heights(2, 3) == [1.15, 1.63]
    assert all_heights(10, 15) == [2.58, 3.65, 4.47, 5.16, 5.77, 6.32, 6.83, 7.3, 7.75, 8.16, 8.56, 8.94, 9.31, 9.66]

def test_all_heights_errors():
    with pytest.raises(ValueError):
        all_heights(0)
    with pytest.raises(SyntaxError):
        all_heights("qwerty")