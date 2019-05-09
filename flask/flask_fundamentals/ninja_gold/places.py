import random
from typing import Callable


class Place(object):
    def __init__(self, name: str, caption: str, action: str, payout: Callable[[], int]):
        self.name = name
        self.caption = caption
        self.payout = payout
        self.action = action

    def find_gold(self) -> int:
        return self.payout()


places = {
    "farm": Place("farm", "Farming is fun, and a bit risky!", "Plant something", lambda: random.randint(0, 3)),
    "cave": Place("cave", "Most caves are empty. but some contain treasure chests fortune.",
                  "Spelunk", lambda: random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100])),
    "house": Place("house", "Ninjas can knit. They are always knit the same thing!",
                   "Knit at home",
                   lambda: 1, ),
    "casino": Place("casino", "You can win big or lose it all.",
                    "Gamble",
                    lambda: random.choice([-50, -20, -6, -1, -1, -3, -1, -3, -4, 5, 8, 3, 22, -1, -3, -5, -2, -10, 1,
                                           1, 50]))
}
