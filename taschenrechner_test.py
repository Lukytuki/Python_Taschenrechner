import unittest
from main import addieren, subtrahieren, multiplizieren, divison

class test_taschenrechner(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtrahieren(self):
        self.assertEqual(subtrahieren(3, 3), 0)
        self.assertEqual(subtrahieren(-1, 1), -2)
        self.assertEqual(subtrahieren(0, 0), 0)

    def test_multiplizieren(self):
        self.assertEqual(multiplizieren(3, 3), 9)
        self.assertEqual(multiplizieren(-1, 2), -2)
        self.assertEqual(multiplizieren(0, 0), 0)

    def test_divison(self):
        self.assertEqual(divison(9, 3), 3)
        self.assertEqual(divison(-1, 2), -0.5)
        self.assertEqual(divison(0, 1), 0)


if __name__ == '__main__':
    unittest.main()
