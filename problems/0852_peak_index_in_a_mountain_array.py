# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# 852. Peak Index in a Mountain Array


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:  # noqa: N802
        # linear
        # for i in range(1, len(arr) - 1):
        #     if arr[i - 1] < arr[i] > arr[i + 1]:
        #         return i
        # return -1
        # logN
        low, high = 0, len(arr) - 1
        while low < high:
            middle = (low + high) // 2
            if arr[middle] < arr[middle + 1]:
                low = middle + 1
            else:
                high = middle
        return low


solution = Solution()


arr = [0, 1, 0]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [0, 2, 1, 0]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [0, 10, 5, 2]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [3, 4, 5, 1]
assert solution.peakIndexInMountainArray(arr) == 2

arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
assert solution.peakIndexInMountainArray(arr) == 2
