from typing import Iterator


class SortedSet:
    def __init__(self) -> None:
        self._set = set[float]()
        self._list = list[float]()

    def add(self, num: float) -> bool:
        if num in self._set:
            return False
        self._set.add(num)
        self._list = sorted(self._list + [num])
        return True

    def contains(self, num: float) -> bool:
        return num in self._set

    def __iter__(self) -> Iterator[float]:
        self._index = 0
        return iter(self._list)

    def __next__(self) -> float:
        if self._index >= len(self._list):
            raise StopIteration
        self._index += 1
        return self._list[self._index - 1]


sorted_set = SortedSet()
assert not sorted_set.contains(1.0)
set_iter = iter(sorted_set)
# print(type(set_iter))  # <class 'list_iterator'>, not SortedSetIterator
assert sorted_set.add(1.0)
assert not sorted_set.add(1.0)
assert sorted_set.contains(1.0)
assert [1.0] == list(sorted_set)
assert sorted_set.add(-1)
assert [-1, 1] == list(sorted_set)
