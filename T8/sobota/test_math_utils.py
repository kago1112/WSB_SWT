import unittest
from math_utils import add

class testAddFunction(unittest.TestCase):
    # testtujemy, czy dodawanie  2+3 jest równe 5
    def test_add_two_numbers(self):
        result = add(2,3)
        self.assertEqual(result, 5) # oczekiwany wynik to 5

if __name__ == '__main__':
    unittest.main()