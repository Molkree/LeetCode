# https://leetcode.com/problems/third-maximum-number/
# 414. Third Maximum Number


class Solution:
    def thirdMax(self, nums: list[int]) -> int:  # noqa: N802
        high = low = mid = -(2**31) - 1
        for num in nums:
            if high < num:
                low, mid, high = mid, high, num
            elif mid < num < high:
                low, mid = mid, num
            elif low < num < mid:
                low = num
        if low != -(2**31) - 1:
            return low
        return high


solution = Solution()


nums = [3, 2, 1]
assert solution.thirdMax(nums) == 1

nums = [1, 2]
assert solution.thirdMax(nums) == 2

nums = [2, 2, 3, 1]
assert solution.thirdMax(nums) == 1

nums = [2, 2, 2]
assert solution.thirdMax(nums) == 2
