# coding=utf-8
"""
Захарченко Евгения, группа КИ19-17/2б
Практическая работа №3, вариант 24: "О равнобедренном треугольнике"

Дан равнобедренный треугольник TR с длиной основания, равной 1, и
высотой, равной H. Задаётся количество частей N, на которые нужно разбить
треугольник TR таким образом, чтобы все части имели одинаковую площадь.
Разбиение можно проводить только прямыми, параллельными основанию
треугольника. Необходимо найти расстояние Si от каждой i-той разбивающей
прямой до вершины треугольника (вершины напротив основания).
"""


import math

def check_height(height) -> float:
    try:
        height = float(height)
    except (TypeError, ValueError):
        raise ValueError('Incorrect value. Write the right answer, please')
    if height <= 0:
        raise ValueError('Incorrect value. The capacity must be a number >= 0')
    return height


def check_num(num) -> int:
    try:
        num = int(num)
    except (TypeError, ValueError):
        raise ValueError('Incorrect value. Write the right answer, please')
    if num <= 0:
        raise ValueError('Incorrect value. The capacity must be a number >= 0')
    return num


def all_heights(height, num):
    # Syntax sugar:
    H = height
    N = num
    all_heights = []

    for i in range(1, N):
        all_heights.append(round(math.sqrt(i) * H / math.sqrt(N), 2))
    return all_heights

def main_program():
    height = input('Set high of triangle: ')
    number = input('Set the number of segments: ')
    height = check_height(height)
    number = check_num(number)
    heights = all_heights(height, number)
    print(heights)

main_program()