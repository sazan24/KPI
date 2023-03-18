# Computer Science FB01, Task 6, Сахній Назар ФБ-01
print("Computer Science FB01, Task 6, варіант 18")
print("Сахній Назар ФБ-01")
ls = [12, 7, -4.4, 8.6, 0, 3, -8, 15, 12.1]
sum_positive, sum_negative = (0, 0)
p = 0
n = 0
for i in range(len(ls)):
    if ls[i] > 0:
        sum_positive += ls[i]
        p += 1
    elif ls[i] < 0:
        sum_negative += ls[i]
        n += 1
# Далі виведення відповіді з урахуванням усіх випадків
if p > 0 and n > 0:
    print("\n2) Кортежем виведено середнє арифметичне додатніх та від'ємних чисел списку ", ls,
 "\n", (float("{:.2f}".format(sum_positive/p)), float("{:.2f}".format(sum_negative/n))), sep="")
elif p > 0 and n == 0:
    print("Оскільки всі елементи в даному списку невід'ємні ", ls, ", то виведено лише\
 значення сер. арифметичного додатніх\n", (float("{:.2f}".format(sum_positive/p))), sep="")
elif p == 0 and n > 0:
    print("Оскільки всі елементи в даному списку недодатні ", ls, ", то виведено лише\
 значення сер. арифметичного від'ємних\n", (float("{:.2f}".format(sum_negative/n))), sep="")
else:
    print("None (список порожній)")
input("\nЩоб вийти із програми, натисність Enter")
