# https://leetcode.com/problems/contiguous-array/
# 525. Contiguous Array


class Solution:
    def findMaxLength(self, nums: list[int]) -> int:  # noqa: N802
        sums = [-1] * (2 * len(nums) + 1)
        sums[len(nums)] = 0
        max_len = 0
        cur_sum = len(nums)
        for i, num in enumerate(nums):
            cur_sum += 1 if num else -1
            if sums[cur_sum] > -1:
                max_len = max(max_len, i - sums[cur_sum] + 1)
            else:
                sums[cur_sum] = i + 1
        return max_len


solution = Solution()


nums = [0, 1]
assert solution.findMaxLength(nums) == 2

nums = [0, 1, 0]
assert solution.findMaxLength(nums) == 2

nums = [0, 0]
assert solution.findMaxLength(nums) == 0

nums = [0, 1, 1]
assert solution.findMaxLength(nums) == 2

nums = [0, 1, 0, 1]
assert solution.findMaxLength(nums) == 4
