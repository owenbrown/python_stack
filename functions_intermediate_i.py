import json
import random
from collections import defaultdict


def rand_int(min: int = 0, max: int = 100) -> int:
    if min > max:
        raise ValueError("min must be greater than max")
    return int(random.random() * (max + 1 - min)) + min


# Testing below

d_1_2 = defaultdict(lambda: 0)
d_1_3 = defaultdict(lambda: 0)
d_0_10 = defaultdict(lambda: 0)
d_5_10 = defaultdict(lambda: 0)

for _ in range(100000):
    d_1_2[rand_int(1, 2)] += 1
    d_1_3[rand_int(1, 3)] += 1
    d_0_10[rand_int(0, 10)] += 1
    d_5_10[rand_int(5, 10)] += 1

print(1, 2)
print(json.dumps(d_1_2, indent=4, sort_keys=True))
print(1, 3)
print(json.dumps(d_1_3, indent=4, sort_keys=True))
print(0, 10)
print(json.dumps(d_0_10, indent=4, sort_keys=True))
print(5, 10)
print(json.dumps(d_5_10, indent=4, sort_keys=True))
