# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray


class Solution:
    def maxProduct(self, nums: list[int]) -> int:  # noqa: N802
        result, max_product, min_product = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            candidates = x, max_product * x, min_product * x
            max_product = max(candidates)
            min_product = min(candidates)
            result = max(result, max_product)
        return result


solution = Solution()


nums = [2, 3, -2, 4]
assert solution.maxProduct(nums) == 6

nums = [-2, 0, -1]
assert solution.maxProduct(nums) == 0

nums = [-2, 3, -4]
assert solution.maxProduct(nums) == 24

nums = [0, 2]
assert solution.maxProduct(nums) == 2

nums = [3, -1, 4]
assert solution.maxProduct(nums) == 4

nums = [-2]
assert solution.maxProduct(nums) == -2

nums = [2, -5, -2, -4, 3]
assert solution.maxProduct(nums) == 24
