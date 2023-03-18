from pythonds.basic.stack import Stack
import string

# Computer Science FB01, Task 4, Сахній Назар ФБ-01
print("Computer Science FB01, Task 4, варіант 18")
print("Сахній Назар ФБ-01")


def polandNote(note):
    prior = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}
    op_stack = Stack()
    finList = []
    startList = note.split()
    for symbol in startList:
        if symbol.isdigit() or symbol in string.ascii_uppercase:
            finList.append(symbol)
        elif symbol == '(':
            op_stack.push(symbol)
        elif symbol == ')':
            topToken = op_stack.pop()
            while topToken != '(':
                finList.append(topToken)
                topToken = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and (prior[op_stack.peek()] >= prior[symbol]):
                finList.append(op_stack.pop())
            op_stack.push(symbol)

    while not op_stack.isEmpty():
        finList.append(op_stack.pop())
    return " ".join(finList)


print(f'Приклади перетворення нормального виразу в зворотній польський запис:\n'
      f'5 + ( ( 1 + 2) * 4 ) - 3\t->\t{polandNote("5 + ( ( 1 + 2 ) * 4 ) - 3")}\n'
      f'( A + B ) - ( D - E ) * ( F + G )\t->\t{polandNote("( A + B ) - ( D - E ) * ( F + G )")}')
your_note = input('Перетворіть свій вираз у постфіксну нотацію (Польський запис):\n')
while your_note != "":
    print(f'Отримаємо: {polandNote(your_note)}\nЩоб вийти із програми, натисність Enter')
    your_note = polandNote(input('\nПеретворіть свій вираз у постфіксну нотацію:\n'))
