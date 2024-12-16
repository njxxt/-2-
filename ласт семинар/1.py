#простите, запоздал с дедлайном(
#остальные дз постараюсь сегодня выложить в гитхаб







import unittest

def prost(n):
    if n <= 0:
        raise ValueError("error")

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors

##################

class test_numbers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prost(1), [])

    def test_2(self):
        self.assertEqual(prost(2), [2])

    def test_3(self):
        self.assertEqual(prost(3), [3])

    def test_4(self):
        self.assertEqual(prost(4), [2, 2])

    def test_18(self):
        self.assertEqual(prost(18), [2, 3, 3])

    def test_29(self):
        self.assertEqual(prost(29), [29])

    def test_100(self):
        self.assertEqual(prost(100), [2, 2, 5, 5])

    def test_12345(self):
        self.assertEqual(prost(12345), [3, 5, 823])

    def test_neg(self):
        with self.assertRaises(ValueError):
            prost(-10)

    def test_0(self):
        with self.assertRaises(ValueError):
            prost(0)

if __name__ == "__main__":
    unittest.main()