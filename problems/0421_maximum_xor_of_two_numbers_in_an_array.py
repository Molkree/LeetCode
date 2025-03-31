# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# 421. Maximum XOR of Two Numbers in an Array


class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:  # noqa: N802
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            masked_nums = {num & mask for num in nums}
            new_max = max_xor | 1 << i
            for masked_num in masked_nums:
                if masked_num ^ new_max in masked_nums:
                    max_xor = new_max
                    break
        return max_xor


solution = Solution()

nums = [3, 10, 5, 25, 2, 8]
assert solution.findMaximumXOR(nums) == 28

nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
assert solution.findMaximumXOR(nums) == 127

nums = [0]
assert solution.findMaximumXOR(nums) == 0

nums = [5, 6, 7]
assert solution.findMaximumXOR(nums) == 3
