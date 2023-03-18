# Computer Science FB01, Task 4.3, Сахній Назар ФБ-01
print("Computer Science FB01, Task 4.3")
print("Сахній Назар ФБ-01")
a = input("\nВведіть число, щоб знайти його квадратний корінь a = ")
x1 = 1  # Будь-яке початкове додатне число
x = x1
n = 1
while not a.isdigit():
    a = input("\nВведіть число, щоб знайти його квадратний корінь a = ")
a = float(a)
while n > 0:
    x = 0.5*(x + a/x)  # Ітераційна ф-ла Герона
    if n == 24:
        break
    n = n + 1
print("\nКвадратний корінь з числа", a, "= {0:.4f}". format(x))
input("\nЩоб вийти із програми, натисність Enter")
