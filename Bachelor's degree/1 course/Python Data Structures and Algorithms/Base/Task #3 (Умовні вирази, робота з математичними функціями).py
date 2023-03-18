# Computer Science FB01, Task 3, Сахній Назар ФБ-01
print("Computer Science FB01, Task 3")
print("Сахній Назар ФБ-01")
x = float(input("\nВведіть число x: "))
z = float(input("Введіть число z: "))
from math import *
if x**2-9 > 0:
    y = abs(x**3-z**3)/sqrt(x**2-9)
    print("18)y=|x^3-z^3|/sqrt(x^2-9)={0:.2f}".format(y))
else:
    print("Помилка при розв'язуванні завдання:\
         \n->Недомустиме значення 'х'")
input("\nЩоб вийти із програми, натисність Enter")

