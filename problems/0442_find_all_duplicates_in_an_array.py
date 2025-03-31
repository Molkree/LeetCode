# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# 442. Find All Duplicates in an Array


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:  # noqa: N802
        result: list[int] = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            nums[abs(num) - 1] *= -1
        return result


solution = Solution()

nums = [4, 3, 2, 7, 8, 2, 3, 1]
assert [2, 3] == solution.findDuplicates(nums)

nums = [1, 1, 2]
assert [1] == solution.findDuplicates(nums)

nums = [1]
assert [] == solution.findDuplicates(nums)
