# Практическая работа №5 по ВвПД

*Основной целью данной практической работы была работа с документацией к функциям*

**Список функций, к которым была написана документация**
* check();
* test_check();
* test_check_errors();
* find_similar();
* test_find_similar();
* test_find_similar_errors();
* triangle();
* test_triangle();
* test_triangle_errors();
* main_program();
* test_main_program();
* test_main_program_errors().

__Алгоритм решения поставленной задачи__
1. Проверить правильность ввода
2. Превратить ввод в список
3. Найти совпадающие числа в списке и удалить их из списка
4. Найти число, удовлетворяющее условию невырожденности треугольника в оставшейся части списка
5. Если число найдено, вывести кортеж чисел, иначе - фразу "Search failed"

Пример рабочего кода:
```python
import pytest

def check(inp):
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
    assert check("5 5 5") == [5, 5, 5]
    assert check("6 6 7 8 9") == [6, 6, 7, 8, 9]

def test_check_errors():
    with pytest.raises(ValueError):
        check("qwerty")
        check("3.5")
        check("-1")
        check("2 3")
    with pytest.raises(AttributeError):
        check(123)

# Find similar elements, if they are here
def find_similar(lst):
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
    assert find_similar([1, 2, 3, 5, 5]) == 5
    assert find_similar([1, 1, 4, 4]) == 1
    assert find_similar([1, 2, 3, 4, 5]) is None

def test_find_similar_errors():
    with pytest.raises(TypeError):
        find_similar(123)
        find_similar("la la la")

def triangle(sim, lst):
    if sim is None:
        return None
    for i in lst:
        x, y, z = [sim, sim, i] if sim >= i else [i, sim, sim]
        if x < y + z:
            return x, y, z
    return None

def test_triangle():
    assert triangle(6, [1, 2, 3]) == (6, 6, 1)
    assert triangle(6, [13, 14, 15]) is None

def test_triangle_errors():
    with pytest.raises(TypeError):
        triangle(6, 5)
        triangle("qwerty")

def main_program(edge):
    edge_right = check(edge)
    seite_1 = find_similar(edge_right)
    print(seite_1)
    answer = triangle(seite_1, edge_right)
    print(answer if answer is not None else 'Search failed')
    return answer

def test_main_program():
    assert main_program("5 5 5") == (5, 5, 5)
    assert main_program("6 6 7 8 9") == (7, 6, 6)
    assert main_program("1 2 3") is None

def test_main_program_errors():
    with pytest.raises(ValueError):
        main_program("qwerty")
        main_program("3.5")
        main_program("-1")
        main_program("2 3")
    with pytest.raises(AttributeError):
        main_program(123)


edge = input("Write the sequence of numbers: ")
main_program(edge)
```

[Правила оформления текста в GitHub](http://webdesign.ru.net/article/pravila-oformleniya-fayla-readmemd-na-github.html)

~Хосспадя, практические закончились, я счастлива~

![Алилуйя](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNzdMxYRi3P2S9DULJ49pjCptWeEoxg5uxhEjW10QhHzbMVSX3&s)
