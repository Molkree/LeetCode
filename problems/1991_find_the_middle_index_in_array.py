# https://leetcode.com/problems/find-the-middle-index-in-array/
# 1991. Find the Middle Index in Array


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:  # noqa: N802
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
