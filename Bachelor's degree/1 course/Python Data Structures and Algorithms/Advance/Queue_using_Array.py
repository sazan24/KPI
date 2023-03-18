class Array_CyclicQueue:
    # Кільцева черга, реалізована через масив

    def __init__(self, size):
        """ Конструктор черги, який створює порожній масив заданої довжини """
        self.head = 0
        self.tail = 0
        self.queue = [None for _ in range(size)]

    def Queue_is_Empty(self) -> bool:
        """ Перевірка на те, чи черга порожня """
        if self.head == self.tail:
            return True
        else:
            return False

    def Queue_is_Full(self) -> bool:
        """ Перевірка на те, чи черга заповнена """
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == len(self.queue) - 1):
            return True
        else:
            return False

    def Enqueue(self, new_item):
        if self.Queue_is_Full():
            print("Черга заповнена, і спроба додати до неї елемент призводить до її переповнення")
            return True
        else:  # Інакше додаєм елемент на відповідну позицію
            self.queue[self.tail] = new_item
            if self.tail == len(self.queue) - 1:
                self.tail = 0
            else:
                self.tail = self.tail + 1
            return None

    def Dequeue(self):
        if self.Queue_is_Empty():
            print("Черга порожня, і при спробі видалити з неї елемент відбувається помилка спустошення")
            return False
        else:  # Інакше видаляємо з неї елемент за принципом "First-In —→ First-Out"
            del_item = self.queue[self.head]
            if self.head == len(self.queue) - 1:
                self.head = 0
            else:
                self.head = self.head + 1
            return del_item

    def outputArray(self):
        print([item for item in self.queue[self.head:self.tail]])

