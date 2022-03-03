# https://leetcode.com/problems/arithmetic-slices/
# 413. Arithmetic Slices


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:  # noqa: N802
        count = 0
        arrays = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] - nums[i] == nums[i] - nums[i + 1]:
                arrays += 1
                count += arrays
            else:
                arrays = 0
        return count


solution = Solution()


nums = [1, 2, 3, 4]
assert solution.numberOfArithmeticSlices(nums) == 3

nums = [1]
assert solution.numberOfArithmeticSlices(nums) == 0

nums = [1, 2, 3, 0, -1, -2]
assert solution.numberOfArithmeticSlices(nums) == 2
