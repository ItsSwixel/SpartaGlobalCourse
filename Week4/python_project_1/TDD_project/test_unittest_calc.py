import unittest
import calculator


class Calctest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)  # add assertion here
        self.assertEqual(calculator.add(12, 15), 27)
        self.assertEqual(calculator.add(-1, 9), 8)
        self.assertEqual(calculator.add(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
