# https://leetcode.com/problems/4sum-ii/
# 454. 4Sum II


from collections import defaultdict


class Solution:
    def fourSumCount(  # noqa: N802
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        sum12 = defaultdict[int, int](int)
        for num1 in nums1:
            for num2 in nums2:
                sum12[num1 + num2] += 1
        result = 0
        for num3 in nums3:
            for num4 in nums4:
                result += sum12[-(num3 + num4)]
        return result


solution = Solution()


nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 2

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
assert solution.fourSumCount(nums1, nums2, nums3, nums4) == 1
