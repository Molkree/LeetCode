# https://leetcode.com/problems/add-binary/
# 67. Add Binary


class Solution:
    def addBinary(self, a: str, b: str) -> str:  # noqa: N802
        return bin(int(a, 2) + int(b, 2))[2:]


solution = Solution()


a = "11"
b = "1"
assert solution.addBinary(a, b) == "100"

a = "1010"
b = "1011"
assert solution.addBinary(a, b) == "10101"
