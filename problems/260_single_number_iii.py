# https://leetcode.com/problems/single-number-iii/
# 260. Single Number III


from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:  # noqa: N802
        xor = 0
        for num in nums:
            xor ^= num
        set_bit = xor & ~(xor - 1)
        num1, num2 = 0, 0
        for num in nums:
            if num & set_bit == set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


solution = Solution()


nums = [1, 2, 1, 3, 2, 5]
assert Counter(solution.singleNumber(nums)) == Counter([3, 5])

nums = [-1, 0]
assert Counter(solution.singleNumber(nums)) == Counter([-1, 0])

nums = [0, 1]
assert Counter(solution.singleNumber(nums)) == Counter([1, 0])
