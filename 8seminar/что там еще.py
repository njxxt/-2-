from collections import Counter
def poli(text):
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())
    freez = Counter(filtered_text)

    sorted_frequency = sorted(freez.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency

key_word = input("Кодовое слово: ")

text = input("Введите текст: ")

freez = poli(text)

print(f"Частота букв '{key_word}':")
for letter, count in freez:
    print(f"{letter}: {count}")

class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщыьэюя"

    def __init__(self, keytable):

        self._encode = {y: x for x, y in zip(self.alphabet, keytable)}
        self._encode.update({y.upper(): x.upper() for x, y in zip(self.alphabet, keytable)})

    def decode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

key = "абвгдеёжзийклмнопрстуфхцчшщыьэюя"
     # абвгдеёжзийклмнопрстуфхцчшщыьэюя
cipher = Monoalphabet(key)

print("Введите текст для расшифровки:")
input_text = input()
encoded_text = cipher.encode(input_text)
print("Расшифрованный текст:", encoded_text)

#дальше я не понял что делать