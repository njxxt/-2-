from collections import Counter
def analyze_frequency(text):
    filtered_text = ''.join(char.lower() for char in text if char.isalpha())

    frequency = Counter(filtered_text)

    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency

#frequency = analyze_frequency(text)
#for letter, count in frequency:
    #print(f"{letter}: {count} раз")


########################

class Monoalphabet:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщыьэюя"

    def __init__(self, keytable):

        self._encode = {y: x for x, y in zip(self.alphabet, keytable)}
        self._encode.update({y.upper(): x.upper() for x, y in zip(self.alphabet, keytable)})

    def decode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

key = "эьормщднйгычясюцажшбтпвёлеъзхкфи"
     # абвгдеёжзийклмнопрстуфхцчшщыьэюя
cipher = Monoalphabet(key)

print("Введите текст для расшифровки:")
input_text = input()
encoded_text = cipher.decode(input_text)

print("Расшифрованный текст:", encoded_text)
