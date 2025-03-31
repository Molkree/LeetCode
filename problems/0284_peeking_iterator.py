# https://leetcode.com/problems/peeking-iterator/
# 284. Peeking Iterator


class Iterator:
    def __init__(self, nums: list[int]) -> None:
        """
        Initializes an iterator object to the beginning of a list.
        """
        self.nums = nums
        self.index = 0

    def hasNext(self) -> bool:  # noqa: N802
        """
        Returns true if the iteration has more elements.
        """
        return self.index < len(self.nums)

    def next(self) -> int:
        """
        Returns the next element in the iteration.
        """
        self.index += 1
        return self.nums[self.index - 1]


class PeekingIterator:
    def __init__(self, iterator: Iterator) -> None:
        self.iterator = iterator
        self.item = self.iterator.next() if self.iterator.hasNext() else -1

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        return self.item

    def next(self) -> int:
        item = self.item
        self.item = self.iterator.next() if self.iterator.hasNext() else -1
        return item

    def hasNext(self) -> bool:  # noqa: N802
        return self.item != -1


peeking_iterator = PeekingIterator(Iterator([1, 2, 3]))
assert peeking_iterator.next() == 1
assert peeking_iterator.peek() == 2
assert peeking_iterator.next() == 2
assert peeking_iterator.next() == 3
assert not peeking_iterator.hasNext()
