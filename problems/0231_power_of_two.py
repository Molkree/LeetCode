# https://leetcode.com/problems/power-of-two/
# 231. Power of Two


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:  # noqa: N802
        # return n > 0 and bin(n).count("1") == 1
        # return n > 0 and n.bit_count() == 1  # Python 3.10+
        return n > 0 and n & (n - 1) == 0


solution = Solution()


n = 1
assert solution.isPowerOfTwo(n)

n = 16
assert solution.isPowerOfTwo(n)

n = 3
assert not solution.isPowerOfTwo(n)

n = -16
assert not solution.isPowerOfTwo(n)

n = 0
assert not solution.isPowerOfTwo(n)
