# Computer Science FB01, Task 7.1, Сахній Назар ФБ-01
print("Computer Science FB01, Task 7.1")
print("Сахній Назар ФБ-01")
x = float(input("\nВведіть число x: "))
z = float(input("Введіть число z: "))


def mod(a):  # Функція для взяття модуля від числа a
    if a >= 0:
        return a
    else:
        return -a


def kor(b):  # Функція для отримання корення з числа b
    k1 = 1
    k = k1
    n = 1
    while n > 0:
        k = 0.5*(k + b/k)  # Ітераційна ф-ла Герона
        if n == 24:
            break
        n = n + 1
    return k
if x**2-9 > 0:
    y = mod(x**3-z**3)/kor(x**2-9)
    print("18) y = |x^3-z^3| / √(x^2-9) = {0:.4f}".format(y))
else:
    print("Помилка при розв'язуванні завдання:\
         \n->Недомустиме значення 'х'")
input("\nЩоб вийти із програми, натисність Enter")
