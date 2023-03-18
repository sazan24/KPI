# Computer Science FB01, Lab 3, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 3, Варіант 18")
print("Сахній Назар ФБ-01")


class Student:
    def __init__(self, surname, name, grades):
        self.surname = surname
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"\nСтудент: {self.surname} {self.name}" \
               f"\nОцінки {{№ семестру: [оцінки]}}: {self.grades}"

    def term_average(self, term):
        try:
            return sum(self.grades[term]) / len(self.grades[term])
        except ZeroDivisionError:
            return "'wrong data'"

    def year_average(self):
        arr = []
        for i in self.grades.keys():
            arr.append(self.term_average(i))
        try:
            return sum(arr) / len(arr)
        except ZeroDivisionError:
            return "'wrong data'"
        except TypeError:
            return "'field [grades] cannot be empty or str type'"

    def set(self, term, marks):
        self.grades[term] = marks

    def get(self, term):
        try:
            return self.grades[term]
        except KeyError:
            return "'cannot find this term'"


first_student = Student('Савчук', 'Володимир', {1: [5, 4, 5, 4, 5], 3: [4, 5, 4, 5, 3]})
print(first_student)  # __str__
print(f'Середній бал за 3-ій семестр: {first_student.term_average(3)}')
print(f'Середнє між середнім усіх семетрів: {first_student.year_average()}')
first_student.set(4, [5, 3, 4])
print(f'Добавимо оцінки за 4-ій семестр: {first_student.grades}')  # Подивитись всі оцінки
print(f'{first_student.get(3)} - оцінки за 3 семестр')

second_student = Student('Бендер', 'Стефан', {1: []})
print(second_student)  # __str__
print(second_student.term_average(1))  # Тут: середнє за 1-ий семестр (*немає*)
print(second_student.year_average())  # Середнє між середнім усіх семетрів (*немає*)
second_student.set(4, [2, 4, 3])  # Додає оціники за 4-ий семестр
print(second_student.grades)  # Подивитись всі оцінки
print(second_student.get(2))  # Тут: переглянути оцінки за 2 семестр, яких нема
input("\nЩоб вийти із програми, натисність Enter")
