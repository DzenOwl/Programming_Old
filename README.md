# Практическая работа №5 по ВвПД

*Основной целью данной практической работы была работа с документацией к функциям*

**Список функций, к которым была написана документация**
* check();
* find_similar();
* triangle();
* main_program();
* и тесты к этому всему.

__Алгоритм решения поставленной задачи__
1. Проверить правильность ввода
3. Найти совпадающие числа в списке 
4. Найти число, удовлетворяющее условию невырожденности треугольника в оставшейся части списка
5. Если число найдено, вывести кортеж чисел, иначе - фразу "Search failed"

Пример рабочего кода:
```python

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
