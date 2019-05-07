import functools
import unittest
from typing import List


# Now that you've learned how to use unittest, let's have you do the following:
#
# reverseList - Write a function that reverses the values in the list (without creating a temporary array).
# Example: reverseList([1,3,5]) should return [5,3,1]
# Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
def reverse_list(values: List):
    if len(values) < 2:
        return
    for i in range(int(len(values) / 2)):
        values[i], values[-(i + 1)] = values[-(i + 1)], values[i]


class ReverseListTests(unittest.TestCase):
    # each method in this class is a test to be run
    def test_empty(self):
        list_1 = []
        reverse_list(list_1)
        self.assertEqual(list_1, [])

    def test_odd(self):
        list_2 = ['a', 'b', 'c']
        reverse_list(list_2)
        self.assertEqual(['c', 'b', 'a'], list_2)

    def test_even(self):
        list_3 = ['a', 'b', 'c', 'd']
        reverse_list(list_3)
        self.assertEqual(['d', 'c', 'b', 'a'], list_3)

    def test_setUp(selfself):
        print("running setup")
        pass

    def tearDown(self):
        pass


# Add at least 3 other test cases
# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same
# backward).
def is_palindrome(word: str) -> bool:
    if not word:
        return False
    for i in range(int(len(word) / 2)):
        if word[i] != word[-(i + 1)]:
            return False
    return True


class IsPalindromeTests(unittest.TestCase):
    def test_racecar(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_rabcr(self):
        self.assertFalse(is_palindrome("rabcr"))

    def test_empty(self):
        self.assertFalse(is_palindrome(str()))

    def test_one_character(self):
        self.assertTrue(is_palindrome("g"))

    def setUp(self):
        pass

    def tearDown(self):
        pass


# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a
# change where you minimize the number of coins you give out.

def coins(cents: int) -> List[int]:
    return [
        int(cents / 25),
        int((cents % 25) / 10),
        int(((cents % 25) % 10) / 5),
        int(cents % 5),
    ]


class TestCoins(unittest.TestCase):
    def testZero(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def testOne(self):
        self.assertEqual(coins(1), [0, 0, 0, 1])

    def testFortyOne(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])

    def testEightySeven(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])


@functools.lru_cache()
def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


class TestFactorial(unittest.TestCase):

    def test_one(self):
        self.assertEqual(fibonacci(1), 0)

    def test_two(self):
        self.assertEqual(fibonacci(2), 1)

    def test_three(self):
        self.assertEqual(fibonacci(3), 1)

    def test_four(self):
        self.assertEqual(fibonacci(4), 2)

    def test_five(self):
        self.assertEqual(fibonacci(5), 3)

    def test_six(self):
        self.assertEqual(fibonacci(6), 5)

    def test_seven(self):
        self.assertEqual(fibonacci(7), 8)


# BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the
# factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
# Example: factorial(5) should return 120.
# Add at least 3 test cases

# BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from
# the sequence. The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the
# previous 2 numbers from the sequence. (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Example: fibonacci(5) should return 3 (the 5th number in the sequence is 3).
# Add at least 3 test cases

if __name__ == '__main__':
    print("junky")
    unittest.main()
