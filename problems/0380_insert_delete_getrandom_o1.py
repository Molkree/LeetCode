# https://leetcode.com/problems/insert-delete-getrandom-o1/
# 380. Insert Delete GetRandom O(1)


import random


class RandomizedSet:
    def __init__(self):
        self.values: list[int] = []
        self.value_to_index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.value_to_index:
            return False
        self.values.append(val)
        self.value_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index:
            return False
        index = self.value_to_index.pop(val)
        last_value = self.values.pop()
        if index < len(self.values):
            self.values[index] = last_value
            self.value_to_index[last_value] = index
        return True

    def getRandom(self) -> int:  # noqa: N802
        return random.choice(self.values)


randomized_set = RandomizedSet()
assert randomized_set.insert(1)
assert not randomized_set.remove(2)
assert randomized_set.insert(2) and randomized_set.values == [1, 2]
assert randomized_set.getRandom() in (1, 2)
assert randomized_set.remove(1) and randomized_set.values == [2]
assert not randomized_set.insert(2)
assert randomized_set.getRandom() == 2
assert randomized_set.getRandom() == 2
