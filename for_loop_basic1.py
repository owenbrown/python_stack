for i in range(151):
    print(i)

for i in range(0, 1001, 5):
    print(i)

for i in range(1, 101):
    print(i)
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")

sum = 0
for i in range(0, 500001):
    sum += i
print(sum)

for i in range(2018, -1, -4):
    print(i)


def flexible_counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1, mult):
        if i % mult == 0:
            print(i)
