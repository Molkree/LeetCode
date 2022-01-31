# https://leetcode.com/problems/domino-and-tromino-tiling/
# 790. Domino and Tromino Tiling


from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:  # noqa: N802
        modulo = 10**9 + 7

        @cache
        def partially_covered(n: int) -> int:
            if n <= 2:
                return 1
            return (partially_covered(n - 1) + fully_covered(n - 2)) % modulo

        @cache
        def fully_covered(n: int) -> int:
            if n <= 2:
                return n
            return (
                fully_covered(n - 1)
                + fully_covered(n - 2)
                + 2 * partially_covered(n - 1)
            ) % modulo

        return fully_covered(n)


solution = Solution()


n = 3
assert solution.numTilings(n) == 5

n = 1
assert solution.numTilings(n) == 1

n = 2
assert solution.numTilings(n) == 2

n = 4
assert solution.numTilings(n) == 11
