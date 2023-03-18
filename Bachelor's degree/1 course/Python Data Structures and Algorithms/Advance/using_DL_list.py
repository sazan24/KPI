import string
import time
import sys

from DoubleLinkedList import *


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


def interaction_with_text(ls):
    # функція для виконання завдання за варіантом
    ls.setFirst()
    first_item = ls.current()

    abc_list = DoublyLinkedList()
    while ls.next():
        if (ls.current() != first_item) and (ls.current() in string.ascii_lowercase) and ls.current().startswith('a'):
            new_item = ls.current()[1:] + "."
            abc_list.insertAtEnd(new_item)
    if abc_list.mFirst:
        print(f"☼ Переглянемо всі такі елементи: ")
        print(f"abc_size ► Об'єм памяті, який займає цей список із 'abc...': {sys.getsizeof(abc_list)} Bytes")
    print(abc_list.outputList(), "\n")


while True:
    my_text = input("\n◘ Напишіть довільний текст наступного типу та формату: \n\
    ▼ Слова тексту із малих латинських літер записані не менше, ніж через один пробіл; Текст закінчується крапкою . \n\
    >>> ")
    if character_check(my_text, "create"):
        array = my_text.split()

        # Заповнення зв'язного списку даними
        dl_list = DoublyLinkedList()
        for item in array:
            dl_list.insertAtEnd(item)
        break

while True:
    input("* Щоб продовжити, натисність |Enter| * \n")
    print("\t\t\t\t    ◄◙► Меню можливих операцій ◄◙►    \n"
          "\t–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––\n"
          "\t| 1. Переглянути двозв'язний список, що складається із слів тексту\n\t|\n"
          "\t| 2. Добавити елемент на початок двозв'язного списку\n"
          "\t| 3. Добавити елемент в кінець двозв'язного списку\n"
          "\t| 4. Добавити елемент у двозв'язний список за заданим індексом\n\t|\n"
          "\t| 5. Видалити перший елемент двозв'язного списку\n"
          "\t| 6. Видалити останній елемент двозв'язного списку\n"
          "\t| 7. Видалити елемент двозв'язного списку за заданим індексом\n\t|\n"
          "\t| 8. Надрукувати всі слова, які відповідають умові 2-го варіанту\n\t|\n"
          "\t∟ 0. Закінчити виконання програми\n")

    option = input("* Щоб виконати необхідну операцію меню, введіть її номер: \n    >>> ")
    if option == "1":
        print("☼ Переглад двозв'язного списку: ")
        start = time.perf_counter()
        print(dl_list.outputList(), "\n")
        stop = time.perf_counter()
        print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
        print(f"time ► Час, за який список виводиться на екран: {stop - start} \n")
    elif option == "2":
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if character_check(new_word, "insert"):
            start = time.perf_counter()
            dl_list.insertAtBegin(new_word)
            stop = time.perf_counter()
            print(f"☼ Переглад двозв'язного списку, у який було додано '{new_word}' на його початок: ")
            print(dl_list.outputList(), "\n")
            print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
            print(f"time ► Час, за який відбується вставка елемента у список: {stop - start} \n")
        else:
            print("Повторіть операцію вставки елемента на початок списку")
    elif option == "3":
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if character_check(new_word, "insert"):
            start = time.perf_counter()
            dl_list.insertAtEnd(new_word)
            stop = time.perf_counter()
            print(f"☼ Переглад двозв'язного списку, у який було додано '{new_word}' в його кінці: ")
            print(dl_list.outputList(), "\n")
            print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
            print(f"time ► Час, за який відбується вставка елемента у список: {stop - start} \n")
        else:
            print("Повторіть операцію вставки елемента в кінець списку")
    elif option == "4":
        index = int(input("◘ Номер позиції, у яку потрібно вставити елемент, це натуральне число: \n\
                      \r\t▼ Який номер позиції списку? \n    >>> "))
        new_word = input("◘ Новий елемент має складатися лише з малих латинських літер [a-z]: \n\
                      \r\t▼ Яке слово необхідно добавити? \n    >>> ")
        if character_check(new_word, "insert"):
            start = time.perf_counter()
            dl_list.insertByIndex(index - 1, new_word)
            stop = time.perf_counter()
            if dl_list.mCurr is not None:
                print(f"☼ Переглад динамічного списку, у який було додано '{new_word}' за заданим індексом '{index}': ")
                print(dl_list.outputList(), "\n")
                print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
                print(f"time ► Час, за який відбується вставка елемента у список: {stop - start} \n")
        else:
            print('Повторіть операцію вставки елемента в список за заданим індексом \n')

    elif option == "5":
        start = time.perf_counter()
        dl_list.deleteAtBegin()
        stop = time.perf_counter()
        if not dl_list.empty():
            print(f"☼ Переглад двозв'язного списку, із початку якого було видалено перший елемент: ")
            print(dl_list.outputList(), "\n")
            print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
            print(f"time ► Час, за який відбується видалення елемента із списку: {stop - start} \n")
    elif option == "6":
        start = time.perf_counter()
        dl_list.deleteAtEnd()
        stop = time.perf_counter()
        if not dl_list.empty():
            print(f"☼ Переглад двозв'язного списку, із кінця якого було видалено останній елемент: ")
            print(dl_list.outputList(), "\n")
            print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
            print(f"time ► Час, за який відбується видалення елемента із списку: {stop - start} \n")
    elif option == "7":
        index = int(input("◘ Номер позиції, елемент якої необхідно видалити, це натуральне число: \n\
                              \r\t▼ Який номер позиції списку? \n    >>> "))
        start = time.perf_counter()
        dl_list.deleteByIndex(index)
        stop = time.perf_counter()
        if not dl_list.empty() and dl_list.mCurr is None:
            print(f"☼ Переглад двозв'язного списку, із якого було видалено елемент за заданим індексом '{index}': ")
            print(dl_list.outputList(), "\n")
            print(f"size ► Об'єм памяті, який займає цей двозв'язний список: {sys.getsizeof(dl_list)} Bytes")
            print(f"time ► Час, за який відбується видалення елемента із чписку: {stop - start} \n")

    elif option == "8":
        start = time.perf_counter()
        interaction_with_text(dl_list)
        stop = time.perf_counter()
        print(f"full_size ► Об'єм памяті, який займає список з усіма словами: {sys.getsizeof(dl_list)} Bytes")
        print(f"time ► Час, за який відбулась ця взаємодія з текстом: {stop - start} \n")
    elif option == "0":
        break
    else:
        print("Неа, такого номера опцерації в меню не існує \n")
