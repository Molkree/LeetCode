# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# 703. Kth Largest Element in a Stream


import bisect
from collections import deque


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        nums.sort()
        self.nums = deque(nums[-k:])
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k or val > self.nums[0]:
            bisect.insort(self.nums, val)
            if len(self.nums) > self.k:
                self.nums.popleft()
        return self.nums[0]


kth_largest = KthLargest(3, [4, 5, 8, 2])
assert kth_largest.add(3) == 4
assert kth_largest.add(5) == 5
assert kth_largest.add(10) == 5
assert kth_largest.add(9) == 8
assert kth_largest.add(4) == 8

kth_largest = KthLargest(1, [])
assert kth_largest.add(-3) == -3
assert kth_largest.add(-2) == -2
assert kth_largest.add(-4) == -2
assert kth_largest.add(0) == 0
assert kth_largest.add(4) == 4

kth_largest = KthLargest(2, [0])
assert kth_largest.add(-1) == -1
assert kth_largest.add(1) == 0
