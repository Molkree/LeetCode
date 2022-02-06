# https://leetcode.com/problems/find-pivot-index/
# 724. Find Pivot Index


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:  # noqa: N802
        left_sum = 0
        right_sum = sum(nums[1:])
        pivot = 0
        for pivot in range(len(nums)):
            if left_sum == right_sum:
                return pivot
            left_sum += nums[pivot]
            if len(nums) > pivot + 1:
                right_sum -= nums[pivot + 1]
        return -1


solution = Solution()


nums = [1, 7, 3, 6, 5, 6]
assert solution.pivotIndex(nums) == 3

nums = [1, 2, 3]
assert solution.pivotIndex(nums) == -1

nums = [2, 1, -1]
assert solution.pivotIndex(nums) == 0

nums = [100, -100]
assert solution.pivotIndex(nums) == -1
