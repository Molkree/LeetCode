# https://leetcode.com/problems/reverse-bits/
# 190. Reverse Bits


class Solution:
    def reverseBits(self, n: int) -> int:  # noqa: N802
        return int("".join(reversed(bin(n)[2:].rjust(32, "0"))), 2)


solution = Solution()


n = 43261596
assert solution.reverseBits(n) == 964176192

n = 4294967293
assert solution.reverseBits(n) == 3221225471
