"""
Захарченко Евгения, группа КИ19-17/2б
Практическая работа №34 вариант 24: "О равнобедренном треугольнике"

Дана последовательность положительных целых чисел EDGE.Необходимо
определить, существует ли в этой последовательности такая тройка элементов S, C и P,
чтобы треугольник с такими сторонами был невырожденным и равнобедренным.
"""
import pytest

def check(inp):
    """
    Проверка ввода.
    Принимает на вход строку из 3 и более целых положительных чисел, разделённых пробелами.
    Проверяет введённые символы на то, что это числа, что они положительные, целые и что их три или больше.

    Arg:
    inp:
        Строка неупорядоченных чисел, разделённых пробелами.

    Returns:
        Список из значений, указанных в строке
    Raises:
    ValueError, AttributeError.

        Examples:
    >>> check("6 6 7 8 9")
    [6, 6, 7, 8, 9]

    >>>check("qwerty")
    Traceback (most recent call last):
        ...
    ValueError: Number is not integer. Write the right answer, please

    >>>check("123")
    Traceback (most recent call last):
        ...
    ValueError: Number is not integer. Write the right answer, please

    >>>check("3.5")
    Traceback (most recent call last):
        ...
    ValueError: Number is not integer. Write the right answer, please

    >>>check("-1")
    Traceback (most recent call last):
        ...
    ValueError: Number is not integer. Write the right answer, please

    >>>check("123")
    Traceback (most recent call last):
        ...
    ValueError: Write 3 or more numbers, please

    >>>check(123)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'split'
    """
    lst = inp.split(" ")
    height = []
    for i in lst:
        if not i.isdigit():
            raise ValueError('Number is not integer. Write the right answer, please')
        try:
            i = int(i)
        except (AttributeError, ValueError):
            raise ValueError('Incorrect value. Write the right answer, please')
        if i <= 0:
            raise ValueError('Incorrect value. The capacity must be a number >= 0')
        if len(lst) < 3:
            raise ValueError('Write 3 or more numbers, please')
        height.append(i)
    return height

def test_check():
    """ Тест проверки ввода.
        Ввод правильных значений.
        Если введена строка из целых положительных чисел в количестве 3+, тест пройден"""
    assert check("5 5 5") == [5, 5, 5]
    assert check("6 6 7 8 9") == [6, 6, 7, 8, 9]

def test_check_errors():
    """ Тест проверки ввода.
        Ввод неправильных значений.
        Если введено что угодно, но не строка из целых положительных чисел в количестве 3+, это ошибка"""
    with pytest.raises(ValueError):
        check("qwerty")
        check("3.5")
        check("-1")
        check("2 3")
    with pytest.raises(AttributeError):
        check(123)

# Find similar elements, if they are here
def find_similar(lst):
    """
    Поиск одинаковых значений в списке.

    Arg:
    inp:
        Строка неупорядоченных чисел, разделённых пробелами.

    Returns:
        Число, на которое были найдены совпадения, либо None, если совпадений найдено не было
    Raises:
        TypeError.

        Examples:
    >>> find_similar([1, 2, 3, 5, 5])
    5

    >>> find_similar([4, 4, 1, 1])
    4

    >>> find_similar([1, 2, 3, 4, 5])
    >>>

    >>> find_similar(123)
    Traceback (most recent call last):
      ...
    TypeError: object of type 'int' has no len()

    >>> find_similar("la la la")
    Traceback (most recent call last):
      ...
    TypeError: 'str' object doesn't support item deletion

    """
    for i in range(1, len(lst)):
#       print("i = ", i)
        for j in range(0, i):
#           print("j = ", j)
            if lst[i] == lst[j]:
#               print(f'{i}: {lst[i]}, {j}: {lst[j]}')
                sim = lst[i]
                del lst[i], lst[j]
                # print(lst)
                return sim
    return None

def test_find_similar():
    """ Тест нахождения совпадений.
        Ввод правильных значений.
        Если введён список, и совпадения в списке найдены, тест пройден"""
    assert find_similar([1, 2, 3, 5, 5]) == 5
    assert find_similar([4, 4, 1, 1]) == 4
    assert find_similar([1, 2, 3, 4, 5]) is None

def test_find_similar_errors():
    """ Тест нахождения совпадений.
        Ввод неправильных значений.
        Если введено что угодно, кроме списка, это ошибка"""
    with pytest.raises(TypeError):
        find_similar(123)
        find_similar("la la la")

def triangle(sim, lst):
    """
    Проверяет треугольник на вырожденность. Если в списке есть сторона:
        а) которая меньше суммы двух одинаковых сторон
        б) которая при сложении с одной из одинаковых сторон даёт результат, больший, чем вторая одинаковая сторона,
    то возвращает список из трёх сторон, иначе возвращает None.

    Args:
    sim: Длина одинаковых сторон
    lst: Список возможных сторон

    Returns:
        x, y, z, если треугольник невырожденный
        None, если треугольник вырожденный

    Raises:
        TypeError

        Examples:
    >>> triangle(6, [1, 2, 3])
    (6, 6, 1)

    >>> triangle(6, [13, 14, 15])
    >>>

    >>> triangle(6, 5)
    Traceback (most recent call last):
      ...
    TypeError: 'int' object is not iterable
    >>> triangle("qwerty")
    Traceback (most recent call last):
      ...
    TypeError: triangle() missing 1 required positional argument: 'lst'
    """
    if sim is None:
        return None
    for i in lst:
        x, y, z = [sim, sim, i] if sim >= i else [i, sim, sim]
        if x < y + z:
            return x, y, z
    return None

def test_triangle():
    """ Тест на вырожденность.
        Ввод правильных значений.
        Если треугольник невырожденный, тест пройден"""
    assert triangle(6, [1, 2, 3]) == (6, 6, 1)
    assert triangle(6, [13, 14, 15]) is None

def test_triangle_errors():
    """ Тест на вырожденность.
        Ввод неправильных значений.
        Если введено что угодно, но не число и список, это ошибка"""
    with pytest.raises(TypeError):
        triangle(6, 5)
        triangle("qwerty")

def main_program(edge):
    """
    Дана последовательность положительных целых чисел EDGE.Необходимо
    определить, существует ли в этой последовательности такая тройка элементов S, C и P,
    чтобы треугольник с такими сторонами был невырожденным и равнобедренным.

    Args:
        edge: строка, состоящая из 3 или более положительных целых чисел.

    Returns:
        answer: кортеж из 3 чисел, если треугольник невырожденный
                None, если треугольник вырожденный

    Raises:
        ValueError.

        Examples:
    >>> main_program("5 5 5")
    5
    (5, 5, 5)
    (5, 5, 5)
    >>> main_program("6 6 7 8 9")
    6
    (7, 6, 6)
    (7, 6, 6)

    >>> main_program("qwerty")
    Traceback (most recent call last):
      ...
    ValueError: Number is not integer. Write the right answer, please

    >>> main_program("3.5")
    Traceback (most recent call last):
      ...
    ValueError: Number is not integer. Write the right answer, please

    >>> main_program("-1")
    Traceback (most recent call last):
      ...
    ValueError: Number is not integer. Write the right answer, please

    >>> main_program("2 3")
    Traceback (most recent call last):
      ...
    ValueError: Write 3 or more numbers, please

    >>> main_program(123)
    Traceback (most recent call last):
      ...
    AttributeError: 'int' object has no attribute 'split'

    >>> main_program([1, 2, 3])
    Traceback (most recent call last):
      ...
    AttributeError: 'list' object has no attribute 'split'

    >>> main_program("1 2 3")
    None
    Search failed
    """
    edge_right = check(edge)
    seite_1 = find_similar(edge_right)
    print(seite_1)
    answer = triangle(seite_1, edge_right)
    print(answer if answer is not None else 'Search failed')
    return answer

def test_main_program():
    """ Тест основной программы.
        Ввод правильных значений.
        Если введена строка из целых положительных чисел в количестве 3+, тест пройден"""
    assert main_program("5 5 5") == (5, 5, 5)
    assert main_program("6 6 7 8 9") == (7, 6, 6)
    assert main_program("1 2 3") is None

def test_main_program_errors():
    """ Тест проверки ввода.
        Ввод неправильных значений.
        Если введено что угодно, но не строка из целых положительных чисел в количестве 3+, это ошибка"""
    with pytest.raises(ValueError):
        main_program("qwerty")
        main_program("3.5")
        main_program("-1")
        main_program("2 3")
    with pytest.raises(AttributeError):
        main_program(123)

edge = input("Write the sequence of numbers: ")
main_program()