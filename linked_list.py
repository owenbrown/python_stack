import unittest


class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None


class SList(object):
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner is None:
            print(runner.value)

    def add_to_back(self, val):
        new_node = Node(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node

    def remove_from_front(self):
        self.head = self.head.next

    def __eq__(self, other: 'SList'):
        self_runner = self.head
        other_runner = other.head

        while True:
            if self_runner is None and other_runner is None:
                return True

            if self_runner is None or other_runner is None:
                return False

            if self_runner.value != other_runner.value:
                return False

            self_runner = self_runner.next
            other_runner = other_runner.next

    def __iter__(self):
        self.__start_node = self.head
        self.__next_node = self.head
        return self

    def __next__(self):

        if self.__next_node is None:
            raise StopIteration
        return_node = self.__next_node
        self.__next_node = self.__next_node.next
        return return_node

    def remove_value(self, value):

        runner = self.head
        while runner:
            if runner is None:
                raise IndexError("value not in Slist")

            if runner.value == value:
                self.head = self.head.next
                return

            runner = runner.next


class TestSlist(unittest.TestCase):
    def setUp(self):
        self.a = SList()
        self.b = SList()
        for c in list("abcdefg"):
            self.a.add_to_front(c)
            self.b.add_to_front(c)

    def test_equality(self):
        self.assertTrue(self.a == self.b)

    def test_not_equal(self):
        self.a.remove_from_front()
        self.assertFalse(self.a == self.b)

    def test_iteration(self):
        collect = list()
        for n in self.a:
            collect.append(n.value)
        self.assertEqual(list("gfedcba"), collect)