# https://leetcode.com/problems/multiply-strings/
# 43. Multiply Strings


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num: str) -> int:
            num_int = 0
            for digit in num:
                num_int = num_int * 10 + ord(digit) - ord("0")
            return num_int

        return str(str_to_int(num1) * str_to_int(num2))


solution = Solution()


num1 = "2"
num2 = "3"
assert solution.multiply(num1, num2) == "6"

num1 = "123"
num2 = "456"
assert solution.multiply(num1, num2) == "56088"

num1 = "0"
num2 = "456"
assert solution.multiply(num1, num2) == "0"
