# АСД -- Лабораторна робота № 2 -- (ФБ-01 Сахній Назар)
# SHELL SORT
from math import log2
import time
from numpy.random import randint

comparisons = 0
moves = 0


def shell_sort(arr):
    global comparisons
    global moves

    distance = []
    for k in range(round(log2(len(arr)) - 1)):
        distance.append(2 * distance[-1] + 1)
    distance.reverse()

    for interval in distance:
        for i in range(interval, len(arr)):  # Виконуємо сортування вставками відповідних підмасивів
            temp = arr[i]
            j = i
            comparisons += 1
            while j >= interval and arr[j - interval] > temp:
                comparisons += 1
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
            moves += 1
    return arr


ls100 = randint(-100, 100, 3)
ls1000 = randint(-1000, 1000, 1000)
ls10000 = randint(-10000, 10000, 10000)
print(f"\n\nДовільний числовий масив із 100 елементів:\n {ls100}")
start = time.time()
print(f"\n\nВідсортований даний масив методом Шелла:\n {shell_sort(ls100)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

print(f"\n\nДовільний числовий масив із 1000 елементів:\n {ls1000}")
start = time.time()
print(f"\n\nВідсортований даний масив методом Шелла:\n {shell_sort(ls1000)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

print(f"\n\nДовільний числовий масив із 10000 елементів:\n {ls10000}")
start = time.time()
print(f"\n\nВідсортований даний масив методом вибору:\n {shell_sort(ls10000)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

