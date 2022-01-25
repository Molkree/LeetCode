# https://leetcode.com/problems/valid-mountain-array/
# 941. Valid Mountain Array


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:  # noqa: N802
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        ind = 1
        while ind + 1 < len(arr) and arr[ind + 1] > arr[ind]:
            ind += 1
        if ind == len(arr) - 1:
            return False
        while ind + 1 < len(arr) and arr[ind + 1] < arr[ind]:
            ind += 1
        return ind == len(arr) - 1


solution = Solution()


arr = [2, 1]
assert not solution.validMountainArray(arr)

arr = [3, 5, 5]
assert not solution.validMountainArray(arr)

arr = [0, 3, 2, 1]
assert solution.validMountainArray(arr)

arr = [1, 2]
assert not solution.validMountainArray(arr)

arr = [1, 2, 2]
assert not solution.validMountainArray(arr)

arr = [1, 2, 1]
assert solution.validMountainArray(arr)

arr = [1, 2, 1, 1]
assert not solution.validMountainArray(arr)

arr = [2, 0, 2]
assert not solution.validMountainArray(arr)

arr = [0, 1, 2]
assert not solution.validMountainArray(arr)
