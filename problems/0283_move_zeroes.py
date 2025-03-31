# https://leetcode.com/problems/move-zeroes/
# 283. Move Zeroes


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:  # noqa: N802
        k = 0
        for i in range(len(nums)):
            num = nums[i]
            if num:
                nums[k] = num
                k += 1
        for i in range(k, len(nums)):
            nums[i] = 0


solution = Solution()


nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0]
solution.moveZeroes(nums)
assert nums == [0]
