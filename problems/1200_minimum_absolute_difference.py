# https://leetcode.com/problems/minimum-absolute-difference/
# 1200. Minimum Absolute Difference


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:  # noqa: N802
        sorted_arr = sorted(arr)
        diffs = [
            abs(sorted_arr[i - 1] - sorted_arr[i]) for i in range(1, len(sorted_arr))
        ]
        min_diff = min(diffs)
        pairs = list[list[int]]()
        for i in range(1, len(arr)):
            if diffs[i - 1] == min_diff:
                pairs.append([sorted_arr[i - 1], sorted_arr[i]])
        return pairs


solution = Solution()


arr = [4, 2, 1, 3]
assert solution.minimumAbsDifference(arr) == [[1, 2], [2, 3], [3, 4]]

arr = [1, 3, 6, 10, 15]
assert solution.minimumAbsDifference(arr) == [[1, 3]]

arr = [3, 8, -10, 23, 19, -4, -14, 27]
assert solution.minimumAbsDifference(arr) == [[-14, -10], [19, 23], [23, 27]]
