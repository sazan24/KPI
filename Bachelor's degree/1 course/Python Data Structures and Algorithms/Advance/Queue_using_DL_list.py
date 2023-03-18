from DoubleLinkedList import *

class DoubleLinked_Queue:
    # Кільцева черга, реалізована через масив

    def __init__(self, size):
        """ Конструктор черги, який створює порожній масив заданої довжини """
        self.head = 0
        self.tail = 0
        self.length = size
        self.queue = DoublyLinkedList()

    def Queue_is_Empty(self) -> bool:
        """ Перевірка на те, чи черга порожня """
        if self.head == self.tail:
            return True
        else:
            return False

    def Queue_is_Full(self) -> bool:
        """ Перевірка на те, чи черга заповнена """
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.length - 1):
            return True
        else:
            return False

    def Enqueue(self, new_item):
        if self.Queue_is_Full():
            print("Черга заповнена, і спроба додати до неї елемент призводить до її переповнення")
            return True
        else:  # Інакше додаєм елемент на відповідну позицію
            self.queue.insertAtEnd(new_item)
            if self.tail == self.length - 1:
                self.tail = 0
            else:
                self.tail = self.tail + 1
            return None

    def Dequeue(self):
        if self.Queue_is_Empty():
            print("Черга порожня, і при спробі видалити з неї елемент відбувається помилка спустошення")
            return False
        else:  # Інакше видаляємо з неї елемент за принципом "First-In —→ First-Out"
            del_item = self.queue.deleteAtBegin()
            if self.head == self.length - 1:
                self.head = 0
            else:
                self.head = self.head + 1
            return del_item
