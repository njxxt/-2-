import sys

class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = {}
        n = len(self.alphabet)
        for i in range(n):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i - key) % n]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()

    def encode(self, text):
        lines = text.splitlines()
        encoded_lines = [
            ''.join([self._encode.get(char, char) for char in line])
            for line in lines
        ]
        return '\n'.join(encoded_lines)


key = int(input('Ээъыцмъ фубз:'))
cipher = Caesar(key)

input_text = sys.stdin.read()
encoded_text = cipher.encode(input_text)
print(encoded_text)