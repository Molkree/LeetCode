# https://leetcode.com/problems/merge-sorted-array/
# 88. Merge Sorted Array


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


solution = Solution()

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
assert [1, 2] == nums1

nums1 = [3, 0, 0]
m = 1
nums2 = [1, 2]
n = 2
solution.merge(nums1, m, nums2, n)
assert [1, 2, 3] == nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution.merge(nums1, m, nums2, n)
assert [1, 2, 2, 3, 5, 6] == nums1

nums1 = [1]
m = 1
nums2: list[int] = []
n = 0
solution.merge(nums1, m, nums2, n)
assert [1] == nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
assert [1] == nums1

nums1 = [1, 2, 4, 5, 6, 0]
m = 5
nums2 = [3]
n = 1
solution.merge(nums1, m, nums2, n)
assert [1, 2, 3, 4, 5, 6] == nums1

nums1 = [1, 2, 4, 5, 6, 0, 0]
m = 5
nums2 = [3, 3]
n = 2
solution.merge(nums1, m, nums2, n)
assert [1, 2, 3, 3, 4, 5, 6] == nums1
