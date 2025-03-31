# https://leetcode.com/problems/rotate-array/
# 189. Rotate Array


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


solution = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
assert [5, 6, 7, 1, 2, 3, 4] == nums

nums = [-1, -100, 3, 99]
k = 2
solution.rotate(nums, k)
assert [3, 99, -1, -100] == nums

nums = [-1]
k = 2
solution.rotate(nums, k)
assert [-1] == nums

nums = [1, 2]
k = 3
solution.rotate(nums, k)
assert [2, 1] == nums
