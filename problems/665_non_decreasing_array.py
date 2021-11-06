# https://leetcode.com/problems/non-decreasing-array/
# 665. Non-decreasing Array


class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:  # noqa: N802
        non_decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if (
                    not non_decreasing
                    or 0 < i < len(nums) - 2
                    and nums[i - 1] > nums[i + 1]
                    and nums[i] > nums[i + 2]
                ):
                    return False
                non_decreasing = False
        return True


solution = Solution()


nums = [4, 2, 3]
assert solution.checkPossibility(nums)

nums = [4, 2, 1]
assert not solution.checkPossibility(nums)

nums = [3, 4, 2, 3]
assert not solution.checkPossibility(nums)

nums = [5, 7, 1, 8]
assert solution.checkPossibility(nums)

nums = [-1, 4, 2, 3]
assert solution.checkPossibility(nums)
