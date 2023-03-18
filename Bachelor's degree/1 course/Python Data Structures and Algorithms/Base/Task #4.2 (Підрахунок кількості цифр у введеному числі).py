# Computer Science FB01, Task 4.2, Сахній Назар ФБ-01
print("Computer Science FB01, Task 4.2")
print("Сахній Назар ФБ-01")
n = int(input("\nКоли введете ціле число n, \
то отримаєте к-ть цифр в ньому\nn = "))
i = 1          
while i > 0:
    if (abs(n) < 10**i):
        q = i  # Виводить кількість цифр
        break
    else:
        i = i + 1
print("К-ть цифр:", q)
input("\nЩоб вийти із програми, натисність Enter")
