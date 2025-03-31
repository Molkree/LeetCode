# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
# 668. Kth Smallest Number in Multiplication Table


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:  # noqa: N802
        def enough(x: int) -> bool:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count >= k

        low, high = 1, m * n
        while low < high:
            middle = (low + high) // 2
            if enough(middle):
                high = middle
            else:
                low = middle + 1
        return low


solution = Solution()


m = 3
n = 3
k = 5
assert solution.findKthNumber(m, n, k) == 3

m = 2
n = 3
k = 6
assert solution.findKthNumber(m, n, k) == 6

m = 9895
n = 28405
k = 100787757
assert solution.findKthNumber(m, n, k) == 31666344
