class Node:
    # Допоміжний клас - вузол двобічно зв'язаного списку """

    def __init__(self, item):
        """ Конструктор вузла

        :param item: Елемент списку
        """
        self.mItem = item  # Дані
        self.mNext = None  # Наступний вузол
        self.mPrev = None  # Попередній вузол


class DoublyLinkedList:
    # Двобічно зв'язаний список

    def __init__(self):
        """ Конструктор списку – створює порожній список """
        self.mFirst = None  # Перший вузол списку
        self.mLast = None   # Останній бузол списку
        self.mCurr = None   # ПОточний бузол списку

    def empty(self):
        """ Перевіряє чи список порожній
        :return: True, якщо список порожній
        """
        return self.mFirst is None

    def setFirst(self):
        """ Зробити поточним перший елемент списку """
        self.mCurr = self.mFirst

    def setLast(self):
        """ Зробити поточним останній елемент списку """
        self.mCurr = self.mLast

    def next(self):
        """ Перейти до наступного елемента """
        if self.mCurr != self.mLast:
            self.mCurr = self.mCurr.mNext
            return True
        else:
            return False

    def prev(self):
        """ Перейти до попереднього елемента """
        if self.mCurr != self.mFirst:
            self.mCurr = self.mCurr.mPrev
            return True
        else:
            return False

    def current(self):
        """ Отримати поточний елемент
        :return: Навантаження поточного вузла
        """
        if self.mCurr is not None:
            return self.mCurr.mItem
        else:
            return None

    def insertAtBegin(self, item):
        """ Можливість вставки елемента елемента на початок списку """
        if self.empty():
            node = Node(item)
            self.mFirst = node
            self.mLast = node
            return
        node = Node(item)
        node.mNext = self.mFirst
        self.mFirst.mPrev = node
        self.mFirst = node

    def insertAtEnd(self, item):
        """ Можливість вставки елемента в кінець списку """
        if self.empty():
            node = Node(item)
            self.mFirst = node
            return
        self.mCurr = self.mFirst
        while self.mCurr.mNext is not None:
            self.mCurr = self.mCurr.mNext
        node = Node(item)
        self.mCurr.mNext = node
        self.mLast = node
        node.mPrev = self.mCurr

    def insertByIndex(self, index, item):
        """ Можливість вставки елемента у список за заданим індексом """
        node = Node(item)
        if self.empty():
            self.mFirst = self.mLast = self.mCurr = node
        else:
            if index <= 0:
                print("Не існує такої позиції у списку \n")
            else:
                self.mCurr = self.mFirst
                n = 1
                while n != index and self.mCurr is not None:
                    self.mCurr = self.mCurr.mNext
                    n += 1
                if self.mCurr is None:
                    print(f"Не можливо вставити елемент, так як позиції під номером '{index}' не існує у списку \n")
                else:
                    node.mPrev = self.mCurr
                    node.mNext = self.mCurr.mNext
                    if self.mCurr.mNext is not None:
                        self.mCurr.mNext.mPrev = node
                    else:
                        self.mLast = node
                    self.mCurr.mNext = node


    def deleteAtBegin(self):
        """ Видалення початкового елементу із списку """
        if self.empty():
            print("Не можливо виконати, так як двозв'язний список не містить жодного елемента \n")
            return None
        if self.mFirst.mNext is None:
            del_item = self.mFirst
            self.mFirst = None
            print("Єдиний елемент двозв'язного списку, що залишився, видалено \n")
            return del_item
        del_item = self.mFirst
        self.mFirst = self.mFirst.mNext
        self.mFirst.mPrev = None
        return del_item

    def deleteAtEnd(self):
        """ Видалення кінцевого елементу зі списку """
        if self.empty():
            print("Не можливо виконати, так як двозв'язний список не містить жодного елемента \n")
            return
        if self.mFirst.mNext is None:
            self.mFirst = None
            print("Єдиний елемент двозв'язного списку, що залишився, видалено \n")
            return
        self.mCurr = self.mFirst
        while self.mCurr.mNext is not None:
            self.mCurr = self.mCurr.mNext
        self.mCurr.mPrev.mNext = None
        self.mCurr = self.mCurr.mPrev
        self.mLast = self.mCurr

    def deleteByIndex(self, index):
        """ Видалення елемента зі списку за заданим індексом """
        if self.empty():
            print("Не можливо виконати, так як двозв'язний список не містить жодного елемента \n")
        else:
            if index <= 0:
                print("Задано неіснуєчий елемент списку \n")
            else:
                self.mCurr = self.mFirst
                n = 1
                while n != index and self.mCurr is not None:
                    self.mCurr = self.mCurr.mNext
                    n += 1
                if self.mCurr is None:
                    print(f"Не можливо видалити елемент, так як елемент під номером '{index}' відсутній у списку \n")
                else:
                    if self.mCurr.mPrev is None:
                        self.mFirst = self.mFirst.mNext
                        self.mFirst.mPrev = None
                        return
                    if self.mCurr.mNext is not None:
                        self.mCurr.mPrev.mNext = self.mCurr.mNext
                        self.mCurr.mNext.mPrev = self.mCurr.mPrev
                        self.mCurr = None
                        return
                    self.mLast = self.mCurr.mPrev
                    self.mCurr.mPrev.mNext = None

    def outputList(self):
        """ Обхід списку та виведення його на екран """
        if self.mFirst is None:
            print("Не можливо виконати, так як двозв'язний список не містить жодного елемента \n")
        else:
            self.mCurr = self.mFirst
            while self.mCurr is not None:
                print(self.mCurr.mItem, end=" <-> ")
                self.mCurr = self.mCurr.mNext
