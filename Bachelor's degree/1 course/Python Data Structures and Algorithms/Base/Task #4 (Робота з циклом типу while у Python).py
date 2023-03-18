# Computer Science FB01, Task 4.1, Сахній Назар ФБ-01
print("Computer Science FB01, Task 4.1")
print("Сахній Назар ФБ-01")
from math import *
n = 2
suma = 0
while n < 17:
    a = pow(n, log(n))/log(n)**n
    n = n + 1
    suma += a 
print("\n18)Знайдена сума 15 членів ряду, у якому \
a=n^ln(n)/(ln(n)^n, n>1:\n", '{0:.4f}'.format(suma))  
input("\nЩоб вийти із програми, натисність Enter")
