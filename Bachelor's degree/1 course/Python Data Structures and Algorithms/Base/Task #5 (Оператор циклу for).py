# Computer Science FB01, Task 5, Сахній Назар ФБ-01
print("Computer Science FB01, Task 5, варіант 18")
print("Сахній Назар ФБ-01")
import numpy as np
from math import *
print("\nВизначити min ф-ії y = sin(x)*x-cos(x) на проміжку:")
c = float(input("від "))
d = float(input("до "))
# minn = 10*4  # можна взяти за мінімум дуже велике значення
minn = sin(c)*c-cos(c)
for x in np.arange(c, d + 10**(-4), 0.001):
    y = sin(x)*x-cos(x)
    # print("{0:.3f}".format(y)) # можна вручну переглянути і переконатись
    if y < minn:
        minn = y
    # min(y, minn) # або ч/з ф-ію мінімуму в Python
print("\nМінімальне значення ф-ії y = sin(x)*x-cos(x) на заданому проміжку: {0:.3f}".format(minn))
input("\nЩоб вийти із програми, натисність Enter")
