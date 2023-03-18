# АСД -- Лабораторна робота № 1 -- (ФБ-01 Сахній Назар)
print('{Знайти НСД двох цілих чисел за алгоритмом Евкліда}')


def euclidean_algorithm(x, y):
    if x == 0:
        return abs(y)
    return euclidean_algorithm(y % x, x)


x, y = map(int, input('\nВведіть два цілих числа через пропуск: ').split())

print(f'НСД чисел {x} та {y}, обчислене рекурсивно за алгоритмом Евкліда,\
 дорівнює: {euclidean_algorithm(x, y)}')

input("\n*Щоб вийти із програми, натисність Enter*")



# АСД -- Лабораторна робота № 1 -- (ФБ-01 Сахній Назар)
print('\n\n{Числа Фібоначчі}')


def fibonacci(n):
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



num = int(input('\nВведіть номер числа: '))

print(f'Маємо, що при n = {num} значення ряду Фібоначчі fn = {fibonacci(num)}')

input("\n*Щоб вийти із програми, натисність Enter*")



# АСД -- Лабораторна робота № 1 -- (ФБ-01 Сахній Назар)
print('\n\n{Ханойські вежі}')


def frame_the_string(move, count):
    width = 9
    print(' ' * len(count) + '*' * width + '\n' + count + '*' + move.center(width - 2) + '*' + '\n' + ' ' * len(count) + '*' * width + '\n')


def hanoi_moves(n, A, B, C):
    global step
    if n == 1:
        step += 1
        frame_the_string(A + ' → ' + C, str(step) + ') ')
    else:
        # Перекласти 'n - 1' дисків зі стрижня 'A' на стрижень 'B'
        # користуючись стрижнем 'C' як допоміжним
        hanoi_moves(n - 1, A, C, B)
        
        # Перекласти 1 диск
        step += 1
        frame_the_string(A + ' → ' + C, str(step) + ') ')
        
        # Перекласти 'n - 1' дисків зі стрижня 'B' на стрижень 'C'
        # користуючись стрижнем 'A' як допоміжним
        hanoi_moves(n - 1, B, A, C)


number_of_disks = int(input('\nВведіть висоту вежі (у дисках): '))

step = 0
hanoi_moves(number_of_disks, 'A', 'B', 'C')

input("\n*Щоб вийти із програми, натисність Enter*")

