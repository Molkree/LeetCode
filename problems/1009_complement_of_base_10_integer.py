# https://leetcode.com/problems/complement-of-base-10-integer/
# 1009. Complement of Base 10 Integer


class Solution:
    def bitwiseComplement(self, n: int) -> int:  # noqa: N802
        return int(bin(n)[2:].translate(str.maketrans({"0": "1", "1": "0"})), 2)


solution = Solution()


num = 5
assert solution.bitwiseComplement(num) == 2

num = 7
assert solution.bitwiseComplement(num) == 0

num = 10
assert solution.bitwiseComplement(num) == 5

num = 0
assert solution.bitwiseComplement(num) == 1
