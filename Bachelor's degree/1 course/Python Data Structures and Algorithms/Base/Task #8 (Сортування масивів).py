# Computer Science FB01, Task 8, Сахній Назар ФБ-01
print("Computer Science FB01, Task 8")
print("Сахній Назар ФБ-01")

# BUBBLE METHOD
def bubble_sortM(B):  # Сортування 1-ої половини списку від меншого до більшого
    # Індекс останнього невідсортованого елемента
    end = len(B)//2 - 1
    while end != 0:
        for i in range(end):
            if B[i] > B[i + 1]:
                B[i], B[i + 1] = B[i + 1], B[i]
        end = end - 1
    return B[:len(B)//2]


def bubble_sortB(M):  # Сортування 2-ої половини списку від більшого до меншого
    # Індекс останнього невідсортованого елемента
    end = len(M) - 1

    while end != 0:
        for i in range(len(M)//2, end):
            if M[i] < M[i + 1]:
                M[i], M[i + 1] = M[i + 1], M[i]
        end = end - 1
    return M[len(M)//2:]

ls = [6, 8, -2, 7, -4.5, 2.4, 8, 1, 82, 0]
print("\nДовільний числовий масив:", ls)
from_M_to_B = bubble_sortM(ls)
from_B_to_M = bubble_sortB(ls)
print("Відсортований даний масив методом бульбашки:", from_M_to_B + from_B_to_M)


# INSERTION SORTING
def insertion_sortM(B):  # Сортування 1-ої половини списку від меншого до більшого
    for i in range(1, len(B)//2):
        j = i-1
        key = B[i]  # Елемент, що вставляється у відсортовану частину списку
        while (B[j] > key) and (j >= 0):
            B[j+1] = B[j]
            j -= 1
        B[j+1] = key
    return B[:len(B)//2]


def insertion_sortB(M):  # Сортування 2-ої половини списку від більшого до меншого
    for i in range(len(M)//2+1, len(M)):
        j = i-1
        key = M[i]  # Елемент, що вставляється у відсортовану частину списку
        while (M[j] < key) and (j >= 0):
            M[j+1] = M[j]
            j -= 1
        M[j+1] = key
    return M[len(M)//2:]
ls = [86, 6, 2.5, 0, -48, 59.99, 4, -54]
print("\nДовільний числовий масив:", ls)
hf_M_to_B = insertion_sortM(ls)
hf_B_to_M = insertion_sortB(ls)
print("Відсортований даний масив методом вставки:", hf_M_to_B + hf_B_to_M)


# SELECTION SORTING
# Сортування 1-ої половини списку від меншого до більшого
def selection_sortM(B):
    for index in range(0, len(B)):
        iSmall = index
        for i in range(index, len(B)//2):  # Пошук індекса min елем. у невідсортованому масиві
            if B[iSmall] > B[i]:
                iSmall = i
        B[index], B[iSmall] = B[iSmall], B[index]
    return B[:len(B)//2]


# Сортування 2-ої половини списку від більшого до меншого
def selection_sortB(M):
    for index in range(len(M)//2, len(M)):
        iSmall = index
        for i in range(index, len(M)):  # Пошук індекса max елем. у невідсортованому масиві
            if M[iSmall] < M[i]:
                iSmall = i
        M[index], M[iSmall] = M[iSmall], M[index]
    return M[len(M)//2:]
ls = [5, 2.4, -8, 0, 89, 542, 80, 45, 4, 42.25, -55]
print("\nДовільний числовий масив:", ls)
print("Відсортований даний масив методом вибору:", selection_sortM(ls) + selection_sortB(ls))



# АСД -- Лабораторна робота № 1 -- (ФБ-01 Сахній Назар)

def shell_Sort(array):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    return array

ls = [5, 2.4, -8, 0, 89, 542, 80, 45, 4, 42.25, -55]
print("\nДовільний числовий масив:", ls)
print("Відсортований даний масив методом Шелла:", shell_Sort(ls))

input("\n*Щоб вийти із програми, натисність Enter*")
