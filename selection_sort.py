from typing import List


def selection_sort(numbers: List[int]):
    if len(numbers) == 1:
        return

    for i in range(len(numbers)):
        smallest_index = i
        # assign i_2 in case 1-item list
        i_2 = i
        for i_2 in range(i + 1, len(numbers)):
            if numbers[smallest_index] > numbers[i_2]:
                smallest_index = i_2
        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]


def test_selection_sort():
    numbers_1 = [3, 4, -3, 33]
    selection_sort(numbers_1)
    assert numbers_1 == [-3, 3, 4, 33]

    numbers_2 = []
    selection_sort(numbers_2)
    assert numbers_2 == []

    numbers_3 = [1]
    selection_sort(numbers_3)
    assert numbers_3 == [1]

    numbers_4 = [-388, 32, -4, 200, 99]
    selection_sort(numbers_4)
    assert numbers_4 == [-388, -4, 32, 99, 200]
