# https://leetcode.com/problems/basic-calculator-ii/
# 227. Basic Calculator II


class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_num = 0
        num = ""
        op = "+"

        def apply_op(char: str) -> None:
            nonlocal op, last_num, num, result
            if op == "*":
                last_num *= int(num)
            elif op == "/":
                last_num = int(last_num / int(num))
            elif op == "-":
                result += last_num
                last_num = -int(num)
            else:
                result += last_num
                last_num = int(num)
            num = ""
            op = char

        for char in s:
            if char.isdigit():
                num += char
            elif char in "+-*/":
                apply_op(char)
        apply_op(op)
        return result + last_num


solution = Solution()


s = "3+2*2"
assert solution.calculate(s) == 7

s = " 3/2 "
assert solution.calculate(s) == 1

s = " 3+5 / 2 "
assert solution.calculate(s) == 5

s = "1+1+1"
assert solution.calculate(s) == 3

s = "0-1*0-1-0"
assert solution.calculate(s) == -1

s = "1+2*5/3"
assert solution.calculate(s) == 4
