# https://leetcode.com/problems/subsets/
# 78. Subsets


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = [[]]
        for num in nums:
            result += [[num] + lst for lst in result]
        return result


solution = Solution()


nums = [0]
# [[],[0]]
print(solution.subsets(nums))

nums = [1, 2, 3]
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(solution.subsets(nums))
