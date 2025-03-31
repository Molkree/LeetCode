# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:  # noqa: N802
        sorted_matrix = sorted(item for row in matrix for item in row)
        return sorted_matrix[k - 1]


solution = Solution()


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
assert solution.kthSmallest(matrix, k) == 13

matrix = [[-5]]
k = 1
assert solution.kthSmallest(matrix, k) == -5
