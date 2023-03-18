from BinarySearchTree import *
import re
import string


def count_and_delete(our_tree, vertex, symbol) -> tuple:
    global counter, draw_again
    if vertex is not None:
        if vertex.key.startswith(symbol.lower()):
            counter += 1
            del_vertex = our_tree.Tree_Delete(vertex)
            if del_vertex.key == our_tree.root.key:
                draw_again.Add_For_Drawing(del_vertex.key)
        else:
            draw_again.Add_For_Drawing(vertex.key)
        count_and_delete(our_tree, vertex.left, symbol)
        count_and_delete(our_tree, vertex.right, symbol)

    return counter, draw_again


while True:
    filepath = input("\n◘ Напишіть абсолютний або відносний шлях до файлу наступного типу та формату: \n\
    ▼ Файл повинен бути текстовим, тобто мати розширення '.txt'\n\
    >>> ")
    try:
        with open(f"{filepath}", "r") as file:
            if filepath.endswith(".txt"):
                text = file.read()
                word_tree = BinarySearchTree()
                draw_tree = DrawBinaryTree()
                print("Список слів із файлу:", re.findall(fr"[\w']+|[{string.ascii_letters}]", text))
                for word in re.findall(fr"[\w']+|[{string.ascii_letters}]", text):
                    word_tree.Tree_Insert(str(word).lower())
                    draw_tree.Add_For_Drawing(str(word).lower())
                print(draw_tree.root)
                print("☼ Центрований (симетричний) обхід бінарного дерева пошуку: \n{", end=" ")
                word_tree.Inorder_Tree_Walk(word_tree.root)
                print("}, де [", word_tree.root.key, "] - це корінь даного дерева.\n", sep="")

                counter = 0
                draw_again = DrawBinaryTree()
                while True:
                    letter = input("\n◘ Щоб визначити Кількість вершин дерева, що містять слова, які починаються "
                                   "на зазначену букву, а опісля Видалити з дерева ці вершини; \n"
                                   "\t▼ Потрібно в не залежності від регістру ввести символ, який є буквою \n"
                                   "\t>>> ")
                    if letter.isalpha():
                        counter, new_tree = count_and_delete(word_tree, word_tree.root, letter)
                        print(f"Кількість таких слів, які починаються із букви '{letter}' -> {counter}")
                        print(new_tree.root)
                        print("☼ Центрований (симетричний) обхід бінарного дерева пошуку: \n{ ", end=" ")
                        word_tree.Inorder_Tree_Walk(word_tree.root)
                        print("}, де [", word_tree.root.key, "] - це корінь даного дерева. \n ", sep="")
                        break
                    else:
                        print("! Символ, який було введено, не є Буквою ! \n")
                break
            else:
                print("Йой, файлове Розширення не відповідає заданому формату! \n")
    except FileNotFoundError:
        print("Ойва, схоже, що було не правильно введено Назву файлу або Шлях до нього! \n")
