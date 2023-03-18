# Computer Science FB01, Task 7.2, Сахній Назар ФБ-01
print("Computer Science FB01, Task 7.2")
print("Сахній Назар ФБ-01")


def A(m, n):  # Функція Акермана
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return A(m-1, 1)
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))
m, n = map(int, input("\nДля ф-ії Акермана введіть ч/з пробіл m і n: ").split())
Akk = A(m, n)
print("A({0:}, {1:}) = {2:}".format(m, n, Akk))
input("\nЩоб вийти із програми, натисність Enter")
