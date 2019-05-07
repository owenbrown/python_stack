import unittest


class Node(object):
    def __init__(self, value, previous_node: 'Node' = None, next_node: 'Node' = None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None  # type: Node
        self.tail = None  # type: Node

    def add_node(self, value, front=False):
        """Adds node to back by default"""
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new

        elif front:
            self.head.previous_node = new
            new.next_node = self.head
            self.head = new

        else:
            self.tail.next_node = new
            new.previous_node = self.tail
            self.tail = new

    def remove_node(self, value):
        """Removes first node with matching value"""
        if self.head is None:
            raise ValueError("DoublyLinkedList is empty")

        runner = self.head  # type Node
        loop_check = False

        while runner:
            if runner.value == value:
                if runner == self.head:
                    self.head = runner.next_node
                if runner == self.tail:
                    self.tail = runner.previous_node

                if runner.previous_node is not None:
                    runner.previous_node.next_node = runner.next_node
                if runner.next_node is not None:
                    runner.next_node.previous_node = runner.previous_node
                return

            if loop_check and self.head == runner:
                raise ValueError()
            runner = runner.next_node
            loop_check = True

    class Iterator(object):
        def __init__(self, dll: 'DoublyLinkedList'):
            self.dll = dll
            self.runner = dll.head

        def __next__(self):
            if self.runner is None:
                raise StopIteration
            return_node = self.runner
            self.runner = self.runner.next_node
            if self.runner == self.dll.head:
                raise StopIteration
            return return_node

    class ReverseIterator(object):
        # Note - objects overly could fall into a linked list.
        def __init__(self, ddl: 'DoublyLinkedList'):
            self.ddl = ddl
            self.runner = ddl.tail

        def __next__(self):
            if self.runner is None:
                raise StopIteration
            return_node = self.runner
            self.runner = self.runner.previous_node
            if self.runner == self.ddl.tail:
                raise StopIteration
            return return_node

    def __iter__(self):
        return self.Iterator(self)

    def insert_after(self, new_value, find_value):
        """Insert after the first instance of value"""
        runner = self.head
        while runner is not None:
            if runner.value == find_value:
                new = Node(new_value, runner, runner.next_node)
                if runner == self.tail:
                    self.tail = new
                if runner.next_node is not None:
                    runner.next_node.previous_node = new
                runner.next_node = new
                return
            runner = runner.next_node
            if runner == self.head:
                # loop
                break
        raise ValueError("value not found")

    def insert_before(self, new_value, find_value):
        """Insert before the first instance of value"""
        runner = self.head
        while runner is not None:
            if runner.value == find_value:
                new = Node(new_value, runner.previous_node, runner)
                if runner == self.head:
                    self.head = new
                if runner.previous_node is not None:
                    runner.previous_node.next_node = new
                runner.previous_node = new
                return
            runner = runner.next_node
            if runner == self.head:
                # loop
                break
        raise ValueError("value not found")

    def reverse(self):
        """Reverse the direction of all nodes in the list"""

    @property
    def values(self):
        return [n.value for n in list(self)]

    def __eq__(self, other: 'DoublyLinkedList'):
        self_runner = self.head
        other_runner = other.head

        while True:
            if self_runner is None and other_runner is None:
                return True

            if self_runner is None or other_runner is None:
                return False

            if self_runner.value != other_runner.value:
                return False

            self_runner = self_runner.next_node
            other_runner = other_runner.next_node


class TestDoublyLinked(unittest.TestCase):
    def setUp(self):
        self.a = DoublyLinkedList()
        self.b = DoublyLinkedList()

        for c in "The quick brown fox jumped":
            self.a.add_node(c)
            self.b.add_node(c)

    def test_equality(self):
        self.assertTrue(self.a == self.b)

    def test_iteration(self):
        values = self.a.values[:5]
        self.assertEqual(list("The q"), values)

    def test_values(self):
        self.assertEqual(list("The quick brown fox jumped"), self.a.values)

    def test_remove(self):
        self.a.remove_node("q")
        self.assertEqual(list("The uick brown fox jumped"), self.a.values)

    def test_insert_after(self):
        self.a.insert_after('Z', 'q')
        self.assertEqual(list("The qZuick brown fox jumped"), self.a.values)

    def test_insert_before(self):
        self.a.insert_before('Z', 'q')
        self.assertEqual(list("The Zquick brown fox jumped"), self.a.values)

    def test_reverse(self):
        self.a.reverse()
        the_list = list("The quick brown fox jumped")
        the_list.reverse()
        self.assertEqual(the_list, self.a.values)
