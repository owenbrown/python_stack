def guess(s: str):
    """Print my guess"""
    print(f"\nI guess:\n{s}. End guess")


# 1
def a():
    return 5


guess("5")
print(a())


# 2
def a():
    return 5


guess("10")
print(a() + a())


# 3
def a():
    return 5
    return 10


guess("5")
print(a())


# 4
def a():
    return 5
    print(10)


guess("5")
print(a())


# 5
def a():
    print(5)


guess("5\nNone")
x = a()
print(x)


# 6
def a(b, c):
    print(b + c)


guess("Exception caught")
try:
    print(a(1, 2) + a(2, 3))
except TypeError as e:
    print("Exception caught")
    print(e)


# 7
def a(b, c):
    return str(b) + str(c)


guess("25")
print(a(2, 5))


# 8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


guess("100\n10")
print(a())


# 9
def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


guess("7")
print(a(2, 3))

guess("14")
print(a(5, 3))

guess("21")
print(a(2, 3) + a(5, 3))


# 10
def a(b, c):
    return b + c
    return 10


guess("8")
print(a(3, 5))

# 11
b = 500
guess("500")
print(b)


def a():
    b = 300
    print(b)


guess("500")
print(b)

guess("300")
a()

guess("500")
print(b)

# 12
b = 500
guess("500")
print(b)


def a():
    b = 300
    print(b)
    return b


guess("500\n300\n500\n500")
print(b)
a()
print(b)
# 13
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


guess("500\n300\n500")
print(b)
b = a()
print(b)


# 14
def a():
    print(1)
    b()
    print(2)


def b():
    print(3)


guess("1\n3\n2")
a()


# 15
def a():
    print(1)
    x = b()
    print(x)
    return 10


def b():
    print(3)
    return 5


guess("1\n3\n5\n10")
y = a()
print(y)
