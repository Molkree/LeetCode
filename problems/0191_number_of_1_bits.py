# https://leetcode.com/problems/number-of-1-bits/
# 191. Number of 1 Bits


class Solution:
    def hammingWeight(self, n: int) -> int:  # noqa: N802
        return n.bit_count()  # Python 3.10+
        return bin(n).count("1")


solution = Solution()

n = 11
assert solution.hammingWeight(n) == 3

n = 128
assert solution.hammingWeight(n) == 1

n = 4294967293
assert solution.hammingWeight(n) == 31
