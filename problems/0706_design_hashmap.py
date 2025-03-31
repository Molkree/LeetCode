# https://leetcode.com/problems/design-hashmap/
# 706. Design HashMap


class MyHashMap:
    def __init__(self) -> None:
        self.mapping = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.mapping[key] = value

    def get(self, key: int) -> int:
        return self.mapping[key]

    def remove(self, key: int) -> None:
        self.mapping[key] = -1


my_hash_map = MyHashMap()
my_hash_map.put(1, 1)
my_hash_map.put(2, 2)
assert my_hash_map.get(1) == 1
assert my_hash_map.get(3) == -1
my_hash_map.put(2, 1)
assert my_hash_map.get(2) == 1
my_hash_map.remove(2)
assert my_hash_map.get(2) == -1
