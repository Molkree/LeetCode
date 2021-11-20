# https://leetcode.com/problems/single-element-in-a-sorted-array/
# 540. Single Element in a Sorted Array


from itertools import accumulate
from operator import xor


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:  # noqa: N802
        low, middle, high = 0, 0, len(nums) // 4
        while low < high:
            middle = (low + high) // 2
            ind = middle * 4
            num_1, num_2, num_3, num_4 = (
                nums[ind],
                nums[ind + 1],
                nums[ind + 2],
                nums[ind + 3],
            )
            if num_1 == num_2 and num_3 == num_4:
                low = middle + 1
            else:
                high = middle
        return list(accumulate(nums[middle * 4 :], xor))[-1]


solution = Solution()


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(solution.singleNonDuplicate(nums))
assert solution.singleNonDuplicate(nums) == 2

nums = [3, 3, 7, 7, 10, 11, 11]
assert solution.singleNonDuplicate(nums) == 10

nums = [1]
assert solution.singleNonDuplicate(nums) == 1
