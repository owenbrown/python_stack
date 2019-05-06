from typing import List


def insertion_sort(numbers: List[int]):
    new_list = list()
    for n in numbers:
        if not new_list:
            new_list = [n]
            print("made new list", new_list)
            continue

        # default case is to tack onto end
        found = False
        for i_2, n_2 in enumerate(new_list):
            print("n, n_2:", n, n_2)
            if n < n_2:
                found = True
                break
            print("new_list", new_list)

        if found:
            print("inserting ", n, "between ", new_list[:i_2], " and ", new_list[i_2:])
            new_list = new_list[:i_2] + [n] + new_list[i_2:]
        else:
            print("appending ", n, " to ", new_list)
            new_list.append(n)
        print()

    for i, n in enumerate(new_list):
        numbers[i] = n


def test_insertion_sort():
    numbers_1 = [3, 4, -3, 33]
    insertion_sort(numbers_1)
    assert numbers_1 == [-3, 3, 4, 33]

    numbers_2 = []
    insertion_sort(numbers_2)
    assert numbers_2 == []

    numbers_3 = [1]
    insertion_sort(numbers_3)
    assert numbers_3 == [1]

    numbers_4 = [-388, 32, -4, 200, 99]
    insertion_sort(numbers_4)
    assert numbers_4 == [-388, -4, 32, 99, 200]
