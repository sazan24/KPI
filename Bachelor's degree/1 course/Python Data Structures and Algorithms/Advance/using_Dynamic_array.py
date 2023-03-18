import string
import time
import sys


def character_check(text, operation):
    # функція для перевірки нових елементів що додаються до списку

    characters = string.ascii_lowercase + " " + "."
    # Перевірка на наявність крапки в кінці тексту
    # Перевірка введених даних, на наявність лише зазначених в змінній chars символів
    if all((symbol in characters) for symbol in text):
        if operation == "create":
            if text.endswith("."):
                print("Файний текст! \n")
                return True
            else:
                print("Оу, щось не видно крапки в кінці рядка! Спробуйте ще раз, але не забудьте про крапку в кінці \n")
                return False
        else:
            return True

    else:
        print("Йой, введений тип даних не відповідає заданому формату! Спробуйте використовувати лише символи [a-z] \n")
        return False


def interaction_with_text(arr):
    # функція для виконання завдання за варіантом
    first_item = arr[0]

    abc_array = []
    for current_item in arr:
        if (current_item != first_item) and (current_item in string.ascii_lowercase) and current_item.startswith('a'):
            new_item = current_item[1:] + "."
            abc_array.append(new_item)
    print(f"☼ Переглянемо всі такі елементи: {abc_array}")
    print(f"abc_size ► Об'єм памяті, який займає цей масив із 'abc...': {sys.getsizeof(abc_array)} Bytes")


while True:
    my_text = input("\n◘ Напишіть довільний текст наступного типу та формату: \n\
    ▼ Слова тексту із малих латинських літер записані не менше, ніж через один пробіл; Текст закінчується крапкою . \n\
    >>> ")
    if character_check(my_text, "create"):
        dyn_array = my_text.split()
        break

while True:
    input("* Щоб продовжити, натисність |Enter| * \n")
    print("\t\t\t\t    ◄◙► Меню можливих операцій ◄◙►    \n"
          "\t–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––\n"
          "\t| 1. Переглянути динамічний масив, що складається із слів тексту\n\t|\n"
          "\t| 2. Добавити елемент на початок динамічного масиву\n"
          "\t| 3. Добавити елемент в кінець динамічного масиву\n"
          "\t| 4. Добавити елемент у динамічний масив за заданим індексом\n\t|\n"
          "\t| 5. Видалити перший елемент динамічного масиву\n"
          "\t| 6. Видалити останній елемент динамічного масиву\n"
          "\t| 7. Видалити елемент динамічного масиву за заданим індексом\n\t|\n"
          "\t| 8. Надрукувати всі слова, які відповідають умові 2-го варіанту\n\t|\n"
          "\t∟ 0. Закінчити виконання програми\n")

    option = input("* Щоб виконати необхідну операцію меню, введіть її номер: \n    >>> ")
    if option == "1":
        print("☼ Переглад динамічного масиву: ", end=" ")
        start = time.perf_counter()
        print(dyn_array)
        stop = time.perf_counter()
        print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
        print(f"time ► Час, за який масив виводиться на екран: {stop - start} \n")
    elif option == "2":
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if character_check(new_word, "insert"):
            start = time.perf_counter()
            dyn_array.insert(0, new_word)
            stop = time.perf_counter()
            print(f"☼ Переглад динамічного масиву, у який було додано '{new_word}' на його початок: {dyn_array}")
            print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
            print(f"time ► Час, за який відбується вставка елемента в масив: {stop - start} \n")
        else:
            print("Повторіть операцію вставки елемента на початок масиву")
    elif option == "3":
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if character_check(new_word, "insert"):
            start = time.perf_counter()
            dyn_array.insert(len(dyn_array), new_word)
            stop = time.perf_counter()
            print(f"☼ Переглад динамічного масиву, у який було додано '{new_word}' в його кінці: {dyn_array}")
            print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
            print(f"time ► Час, за який відбується вставка елемента в масив: {stop - start} \n")
        else:
            print("Повторіть операцію вставки елемента в кінець масиву")
    elif option == "4":
        index = int(input("◘ Номер позиції, у яку потрібно вставити елемент, це натуральне число: \n\
                      \r\t▼ Який номер позиції масиву? \n    >>> "))
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if 0 < index < len(dyn_array):
            if character_check(new_word, "insert"):
                start = time.perf_counter()
                dyn_array.insert(index - 1, new_word)
                stop = time.perf_counter()
                print(f"☼ Переглад динамічного масиву, у який було додано '{new_word}' за заданим індексом '{index}': "
                      f"{dyn_array}")
                print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
                print(f"time ► Час, за який відбується вставка елемента в масив: {stop - start} \n")
            else:
                print('Повторіть операцію вставки елемента в масив за заданим індексом \n')
        else:
            print("Схоже, що така позиція масиву, в яку потрібно вставити елемент, не існує \n")
    elif option == "5":
        if not dyn_array:
            print("Не можливо виконати, так як динамічний масив не містить жодного елемента \n")
        else:
            start = time.perf_counter()
            dyn_array.pop(0)
            stop = time.perf_counter()
            print(f"☼ Переглад динамічного масиву, із початку якого було видалено перший елемент: {dyn_array}")
            print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
            print(f"time ► Час, за який відбується видалення елемента із масиву: {stop - start} \n")
    elif option == "6":
        if not dyn_array:
            print("Не можливо виконати, так як динамічний масив не містить жодного елемента \n")
        else:
            start = time.perf_counter()
            dyn_array.pop()
            stop = time.perf_counter()
            print(f"☼ Переглад динамічного масиву, із кінця якого було видалено останній елемент: {dyn_array}")
            print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
            print(f"time ► Час, за який відбується видалення елемента із масиву: {stop - start} \n")
    elif option == "7":
        index = int(input("◘ Номер позиції, елемент якої необхідно видалити, це натуральне число: \n\
                              \r\t▼ Який номер позиції масиву? \n    >>> "))
        if 0 < index < len(dyn_array):
            if not dyn_array:
                print("Не можливо виконати, так як динамічний масив не містить жодного елемента \n")
            else:
                start = time.perf_counter()
                dyn_array.pop(index - 1)
                stop = time.perf_counter()
                print(f"☼ Переглад динамічного масиву, із якого було видалено елемент за заданим індексом '{index}': "
                      f"{dyn_array}")
                print(f"size ► Об'єм памяті, який займає цей динамічний масив: {sys.getsizeof(dyn_array)} Bytes")
                print(f"time ► Час, за який відбується видалення елемента із масиву: {stop - start} \n")
        else:
            print("Схоже, що така позиція масиву, елемент якої необхідно видалити, не існує \n")
    elif option == "8":
        if not dyn_array:
            print("Не можливо виконати, так як динамічний масив не містить жодного елемента \n")
        else:
            start = time.perf_counter()
            interaction_with_text(dyn_array)
            stop = time.perf_counter()
            print(f"full_size ► Об'єм памяті, який займає масив з усіма словами: {sys.getsizeof(dyn_array)} Bytes")
            print(f"time ► Час, за який відбулась ця взаємодія з текстом: {stop - start} \n")
    elif option == "0":
        break
    else:
        print("Неа, такого номера опцерації в меню не існує")
