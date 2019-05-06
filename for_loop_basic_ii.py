# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
from typing import Dict, List, Union


def biggie_size(numbers: List[int]) -> List[Union[int, str]]:
    for i, n in enumerate(numbers):
        if n > 0:
            numbers[i] = "big"

    return numbers


def test_biggie_size():
    assert biggie_size([-1, 3, 5, -5]) == [-1, "big", "big", -5]


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive
# values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(numbers: List[int]):
    if not numbers:
        return
    positives = 0
    for n in numbers:
        if n > 0:
            positives += 1
    numbers[-1] = positives


def test_count_positives():
    numbers_1 = [-1, 1, 1, 1]
    count_positives(numbers_1)
    assert numbers_1 == [-1, 1, 1, 3]

    numbers_2 = [1, 6, -4, -2, -7, -2]
    count_positives(numbers_2)
    assert numbers_2 == [1, 6, -4, -2, -7, 2]


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(values: List[int]) -> int:
    return sum(values)


def test_sum_total():
    assert sum_total([1, 2, 3, 4]) == 10
    assert sum_total([6, 3, -2]) == 7


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(values: List[int]) -> float:
    if not values:
        return 0
    return float(sum(values)) / float(len(values))


def test_average():
    assert average([1, 2, 3, 4]) == 2.5


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(items: list) -> int:
    return len(items)


def test_length():
    assert length([37, 2, 1, -9]) == 4
    assert length([]) == 0


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is
# empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(numbers: List[int]) -> int:
    if not numbers:
        return False
    return min(numbers)


def test_minimum():
    assert minimum([37, 2, 1, -9]) == -9
    assert minimum([]) is False


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have
# the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(values: List[int]) -> int:
    if not values:
        return False
    return max(values)


def test_maximum():
    assert maximum([37, 2, 1, -9]) == 37
    assert maximum([]) == False


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average,
# minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37,
# 'length': 4 }

def ultimate_analysis(numbers: List[int]) -> Union[bool, Dict[str, Union[int, float]]]:
    if not numbers:
        return False
    return {
        "sumTotal": sum(numbers),
        "average": average(numbers),
        "minimum": minimum(numbers),
        "maximum": maximum(numbers),
        "length": len(numbers)
    }


def test_ultimate_analysis():
    assert ultimate_analysis([37, 2, 1, -9]) == {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37,
                                                 'length': 4}


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without
# creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(numbers: List[int]):
    for i in range(int(len(numbers) / 2)):
        print(i)
        numbers[i], numbers[-i - 1] = numbers[-i - 1], numbers[i]


def test_reverse_list():
    numbers = [37, 2, 1, -9]
    reverse_list(numbers)
    assert numbers == [-9, 1, 2, 37]
