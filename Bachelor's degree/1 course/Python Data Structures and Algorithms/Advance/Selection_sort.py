# АСД -- Лабораторна робота № 2 -- (ФБ-01 Сахній Назар)
# SELECTION SORT
import time
from numpy.random import randint

comparisons = 0
moves = 0


def selection_sort(arr):
    global comparisons
    global moves

    for index in range(len(arr) - 1):
        min_value = index
        for search in range(index + 1, len(arr)):  # Пошук індекса min елемента у невідсортованому масиві
            comparisons += 1
            if arr[search] < arr[min_value]:
                min_value = search  # Оновлюємо індекс min елемента
        arr[index], arr[min_value] = arr[min_value], arr[index]  # Міняємо місцями з першим невідсортованим елементом
        moves += 1
    return arr


ls100 = randint(-100, 100, 3)
ls1000 = randint(-1000, 1000, 1000)
ls10000 = randint(-10000, 10000, 10000)
print(f"\n\nДовільний числовий масив із 100 елементів:\n {ls100}")
start = time.time()
print(f"\n\nВідсортований даний масив методом вибору:\n {selection_sort(ls100)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

print(f"\n\nДовільний числовий масив із 1000 елементів:\n {ls1000}")
start = time.time()
print(f"\n\nВідсортований даний масив методом вибору:\n {selection_sort(ls1000)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

print(f"\n\nДовільний числовий масив із 10000 елементів:\n {ls10000}")
start = time.time()
print(f"\n\nВідсортований даний масив методом вибору:\n {selection_sort(ls10000)}"
      f"\n\nКількість ОБМІНІВ: {moves}, ПОРІВНЯНЬ: {comparisons}"
      f"\nЧас сортування {time.time() -  start}")

#0.0010175704956054688
