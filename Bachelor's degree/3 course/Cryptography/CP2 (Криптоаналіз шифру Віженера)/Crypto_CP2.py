# *****************          Preparation section          *****************
plain_text = open('./wisdom.txt', 'r', encoding="utf-8").read()
cipher_text = open('./cipher.txt', 'r', encoding="utf-8").read()
plain_text_size = len(plain_text)
cipher_text_size = len(cipher_text)
indexes_of_encryption = open("./indexes_of_encryption_part.txt", "w")
indexes_of_decryption = open("./indexes_of_decryption_part.txt", "w")
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_length = len(alphabet)
alphabet_numbers = dict(zip(alphabet, [i for i in range(alphabet_length)]))
chars_count_pattern = dict(zip(alphabet, [0] * alphabet_length))
key_words = ["шо", "чат", "нора", "корок", "литература", "аккумулятор", "самодержавие", "товароведение",
             "книгохранилище", "машиностроитель", "жизнеобеспечение", "хлебозаготовитель", "тяжелоатлетический",
             "шапкозакидательство", "золотопромышленность"]


# *****************          Functions          *****************
def count_index(values, text_size):
    I = 0
    for number in values:
        I += number * (number - 1)
    return I / (text_size * (text_size - 1))


def count_char_in_text(text, to_return):
    for letter in text:
        to_return[letter] += 1
    return to_return


# *****************          Encryption section          ******************
for key in key_words:
    key_length = len(key)
    answer = open(str(key_length) + "_key.txt", "w")
    chars_count = chars_count_pattern.copy()
    for i in range(plain_text_size):
        new_number = (alphabet_numbers[plain_text[i]] + alphabet_numbers[key[i % key_length]]) % alphabet_length
        char = alphabet[new_number]
        chars_count[char] += 1
        answer.write(char)
    answer.close()
    indexes_of_encryption.write(str(key_length) + "-key index: " + str(count_index(chars_count.values(), plain_text_size)) + '\n')
print("♣ The 'plain_text.txt' was encrypted with the Vigenère cipher using different key lengths")
chars_count_main = count_char_in_text(plain_text, chars_count_pattern.copy())
indexes_of_encryption.write("Plaintext index: " + str(count_index(chars_count_main.values(), plain_text_size)) + '\n')
indexes_of_encryption.close()
print("✔ The indexes of coincidence for 'plain_text.txt' were written to the file 'indexes_of_encryption_part.txt'")

# *****************          Decryption section part_1 key_length          ******************
indexes_of_keys = []
for i in range(2, 35):
    index_of_key = 0
    for j in range(i):
        t = cipher_text[j::i]
        chars_count_in_part = count_char_in_text(t, chars_count_pattern.copy())
        index_of_key += count_index(chars_count_in_part.values(), len(t))
    indexes_of_keys += [[i, index_of_key / i]]
    indexes_of_decryption.write(str(i) + "-key: " + str(index_of_key / i) + '\n')
max_index = max([i[1] for i in indexes_of_keys])
might_indexes = [i for i in indexes_of_keys if max_index - i[1] < max_index / 10]
for x in might_indexes:
    indexes_of_decryption.write("A " + str(x[0]) + " symbols is a possible key length with " + str(x[1]) + " index.\n")
indexes_of_decryption.close()
print("✔ The indexes of coincidence for 'cipher_text.txt' were written to the file 'indexes_of_decryption_part.txt'\n")
# *****************          Decryption section part_2 Caesar_decryption          ******************
alphabet_sorted_by_possibility = ['о', 'а', 'е', 'и', 'н', 'т', 'л', 'с', 'р', 'в', 'к', 'у', 'м', 'п', 'д', 'г', 'я', 'з',
                                  'ы', 'ъ', 'ч', 'б', 'й', 'ж', 'ш', 'х', 'ю', 'щ', 'ц', 'э', 'ф', 'ь']
key_length = might_indexes[0][0]
key_answer = [''] * key_length
the_most_frequent_letters = []
for i in range(key_length):
    text = cipher_text[i::key_length]
    counts = count_char_in_text(text, chars_count_pattern.copy())
    the_most_frequent_letters += [max(counts, key=counts.get)]
possible = [0] * key_length
while True:
    decrypted_text_list = list(cipher_text)
    decrypted_text_size = len(decrypted_text_list)
    for j in range(key_length):
        possible_variant = (alphabet_numbers[the_most_frequent_letters[j]] - alphabet_numbers[
            alphabet_sorted_by_possibility[possible[j]]]) % alphabet_length
        char = alphabet[possible_variant]
        for x in range(j, decrypted_text_size, key_length):
            decrypted_text_list[x] = alphabet[
                (alphabet_numbers[decrypted_text_list[x]] - alphabet_numbers[char]) % alphabet_length]
        key_answer[j] = char
        decrypted = open("./decrypted_text.txt", "w")
        decrypted.write("".join(decrypted_text_list))
        decrypted.close()
    print("Current possible key:", key_answer)
    print("◘ Which symbol in key should be changed?")
    possible[int(input(">>> ")) - 1] += 1
