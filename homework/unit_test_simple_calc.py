import unittest
import test_simple_calc as calc


class MyTestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(8, 1), 9)
        with self.assertRaises(TypeError):
            calc.add('s', 7)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        with self.assertRaises(TypeError):
            calc.subtract(7, '5')

    def test_divide(self):
        self.assertEqual(calc.divide(12, 3), 4)
        with self.assertRaises(ValueError):
            calc.divide(8, 0)
        with self.assertRaises(TypeError):
            calc.divide('7', '8')

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 5), 15)
        with self.assertRaises(TypeError):
            calc.multiply('4', 'err')


if __name__ == '__main__':
    unittest.main()
