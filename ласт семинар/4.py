import sys
import unittest

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


if __name__ == "__main__":
    key = int(input("Введите ключ: "))
    cipher = Caesar(key)
    input_text = sys.stdin.read()
    encoded_text = cipher.encode(input_text)
    print(encoded_text)


#########


class test(unittest.TestCase):
    def test_1(self):
        cipher = Caesar(1)
        input_text = "абв"
        expected_output = "бвг"
        self.assertEqual(cipher.encode(input_text), expected_output)

    def test_5(self):
        cipher = Caesar(28)
        input_text = "жу цтй ёехиеп н ж зуружй ёехиеп"
        expected_output = "во сне бардак и в голове бардак"
        self.assertEqual(cipher.encode(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()