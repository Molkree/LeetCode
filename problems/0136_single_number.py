# https://leetcode.com/problems/single-number/
# 136. Single Number


import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> int:  # noqa: N802
        # functional way
        return reduce(operator.xor, nums, 0)
        # regular way
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number


solution = Solution()


nums = [2, 2, 1]
assert solution.singleNumber(nums) == 1

nums = [4, 1, 2, 1, 2]
assert solution.singleNumber(nums) == 4

nums = [1]
assert solution.singleNumber(nums) == 1
