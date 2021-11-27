# https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self


from itertools import accumulate
from operator import mul


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:  # noqa: N802
        # O(n) space
        products: list[int] = list(accumulate(nums, mul, initial=1)) + list(
            reversed(list(accumulate(nums[::-1], mul, initial=1)))
        )
        result: list[int] = []
        nums_count = len(nums)
        for index in range(nums_count):
            before = products[index]
            after = products[nums_count + index + 2]
            product = before * after
            result.append(product)
        return result
        # O(1) space (if we don't count result)
        result: list[int] = []
        product = 1
        for i in range(len(nums)):
            result.append(product)
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result


solution = Solution()


nums = [1, 2, 3, 4]
assert solution.productExceptSelf(nums) == [24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]
assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]
