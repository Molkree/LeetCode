# https://leetcode.com/problems/design-hashset/
# 705. Design HashSet


class MyHashSet:
    def __init__(self) -> None:
        self.buckets = [False] * 1000001

    def add(self, key: int) -> None:
        self.buckets[key] = True

    def remove(self, key: int) -> None:
        self.buckets[key] = False

    def contains(self, key: int) -> bool:
        return self.buckets[key]


my_hash_set = MyHashSet()
my_hash_set.add(1)
my_hash_set.add(2)
assert my_hash_set.contains(1)
assert not my_hash_set.contains(3)
my_hash_set.add(2)
assert my_hash_set.contains(2)
my_hash_set.remove(2)
assert not my_hash_set.contains(2)
