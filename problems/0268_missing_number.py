# https://leetcode.com/problems/missing-number/
# 268. Missing Number


class Solution:
    def missingNumber(self, nums: list[int]) -> int:  # noqa: N802
        return (set(range(len(nums) + 1)) - set(nums)).pop()


solution = Solution()


nums = [3, 0, 1]
assert solution.missingNumber(nums) == 2

nums = [0, 1]
assert solution.missingNumber(nums) == 2

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
assert solution.missingNumber(nums) == 8
