# https://leetcode.com/problems/single-number-ii/
# 137. Single Number II


class Solution:
    def singleNumber(self, nums: list[int]) -> int:  # noqa: N802
        x1, x2, mask = 0, 0, 0
        for num in nums:
            x2 ^= x1 & num
            x1 ^= num
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1


solution = Solution()


nums = [3, 3, 2, 3]
assert solution.singleNumber(nums) == 2

nums = [2, 2, 3, 2]
assert solution.singleNumber(nums) == 3

nums = [0, 1, 0, 1, 0, 1, 99]
assert solution.singleNumber(nums) == 99
