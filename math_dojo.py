import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


class TestMathDojo(unittest.TestCase):

    def setUp(self):
        self.md = MathDojo()

    def test_add_subtract(self):
        self.assertEqual(self.md.add(2).add(2, 5, 1).subtract(3, 2).result, 5)

    def test_add(self):
        self.assertEqual(self.md.add(2).result, 2)


if __name__ == '__main__':
    unittest.main()
