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
        
    def test_multip(self):
        self.assertEqual(self.calc.multip(10,2),20)
        self.assertEqual(self.calc.multip(14,2),28)
        self.assertEqual(self.calc.multip(82,3),246)
        self.assertEqual(self.calc.multip(31,5),155)
        self.assertEqual(self.calc.multip(36,6),216)
        
if __name__ == "__main__":
    unittest.main()