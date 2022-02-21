# https://leetcode.com/problems/sort-array-by-parity/
# 905. Sort Array By Parity


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:  # noqa: N802
        odd_index = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[odd_index], nums[i] = nums[i], nums[odd_index]
                odd_index += 1
        return nums
