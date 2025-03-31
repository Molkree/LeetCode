# https://leetcode.com/problems/number-complement/
# 476. Number Complement


class Solution:
    def findComplement(self, num: int) -> int:  # noqa: N802
        translation = str.maketrans({"0": "1", "1": "0"})
        return int(bin(num)[2:].translate(translation), 2)


solution = Solution()


num = 5
assert solution.findComplement(num) == 2

num = 1
assert solution.findComplement(num) == 0
