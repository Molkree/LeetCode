# https://leetcode.com/problems/sort-colors/
# 75. Sort Colors


class Solution:
    def sortColors(self, nums: list[int]) -> None:  # noqa: N802
        zero_index = 0
        one_index = 0
        two_index = len(nums) - 1
        while one_index <= two_index:
            if nums[one_index] < 1:
                nums[zero_index], nums[one_index] = nums[one_index], nums[zero_index]
                zero_index += 1
                one_index += 1
            elif nums[one_index] > 1:
                nums[one_index], nums[two_index] = nums[two_index], nums[one_index]
                two_index -= 1
            else:
                one_index += 1


solution = Solution()


nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
assert [0, 0, 1, 1, 2, 2] == nums

nums = [2, 0, 1]
solution.sortColors(nums)
assert [0, 1, 2] == nums

nums = [0]
solution.sortColors(nums)
assert [0] == nums

nums = [1]
solution.sortColors(nums)
assert [1] == nums

nums = [1, 2, 0]
solution.sortColors(nums)
assert [0, 1, 2] == nums
