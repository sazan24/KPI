# Computer Science FB01, Lab 2, Сахній Назар ФБ-01
print("Computer Science FB01, Lab 2, варіант 18")
print("Сахній Назар ФБ-01")
import string
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
text = '''Перевірка якості зв'язку Inthernet мережі, щоб переглянути фільм "Iron Man 3". Яка швидкість зв'язку Inthernet?!.
                Inthernet - це всесвітня мережа#%@'''
print("\nДаний текст:\n", text)
for word in text.lower().split():  # Обрахунок кількості кожного слова
    word = word.strip(strip)
    if len(word) > 2:
        words[word] = words.get(word, 0) + 1
print("\nСлова, що зустрічаються в цьому тексті лише 1 раз:")
for word in sorted(words):  # Вивід тих слів, що зустрічаються 1 раз
    if words[word] == 1:
        print("'{0}'".format(word))
input("\nЩоб вийти із програми, натисність Enter")
