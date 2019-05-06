class Underscore:
    def map(self, iterable, callback):
        return map(callback, iterable)

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i
        return None

    def filter(self, iterable, callback):
        return [i for i in iterable if callback(i)]

    def reject(self, iterable, callback):
        return [i for i in iterable if not callback(i)]


# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore()  # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)


# should return [2, 4, 6] after you finish implementing the code above


def test_underscore():
    u_1 = Underscore()
    assert u_1.map([1, 2, 3], lambda x: x * 2) == [2, 4, 6]
    assert u_1.find([1, 2, 3, 4, 5, 6], lambda x: x > 4) == 5
    assert u_1.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) == [2, 4, 6]
    assert u_1.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0) == [1, 3, 5]
