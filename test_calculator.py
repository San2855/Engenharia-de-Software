import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10,2),5)
        self.assertEqual(self.calc.divisao(8,2),4)
        self.assertEqual(self.calc.divisao(18,3),6)
        self.assertEqual(self.calc.divisao(25,5),5)
        self.assertEqual(self.calc.divisao(36,6),6)

    def test_multip(self):
        self.assertEqual(self.calc.multip(10,2),20)
        self.assertEqual(self.calc.multip(14,2),28)
        self.assertEqual(self.calc.multip(82,3),246)
        self.assertEqual(self.calc.multip(31,5),155)
        self.assertEqual(self.calc.multip(36,6),216)
        
if __name__ == "__main__":
    unittest.main()