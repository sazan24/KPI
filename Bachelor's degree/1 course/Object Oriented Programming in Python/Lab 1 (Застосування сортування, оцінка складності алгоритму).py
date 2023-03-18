# Computer Science FB01, Lab 1, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 1, варіант 18")
print("Сахній Назар ФБ-01")
from random import randrange


def shift(ls, k):
    if k < 0:
        k = abs(k)
        for i in range(k):
            ls.append(ls.pop(0))
    else:
        for i in range(k):
            ls.insert(0, ls.pop())
print("\nЗа допомогою цього коду можна циклічно переставити всі N елементів списку, заданих довільними числами на проміжку [a, b), на k позицій.")
N = int(input("\nВведіть кількість елементів списку N = "))
a = float(input("на проміжку від a = "))
b = float(input("до b = "))
ls = []
if (N > 0) & (a < b):
    for i in range(N):
        ls.append(round(randrange(10*a, 10*b)/10, 1))  # b-(b-a)*random.random()
    print("Отримали довільний список:", ls)
    k = int(input("\n↓Якщо ввести k > 0, то елементи зсунуться вправо, а якщо k < 0, то вліво \nk = "))

    shift(ls, k)
    print("Маємо:",ls)
else:
    print("\nПомилка → Не правильно заданий діапазон чисел")
input("\nЩоб вийти із програми, натисність Enter")
