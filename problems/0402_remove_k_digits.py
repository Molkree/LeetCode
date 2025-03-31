# https://leetcode.com/problems/remove-k-digits/
# 402. Remove K Digits


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:  # noqa: N802
        if k == len(num):
            return str(0)
        stack = [num[0]]
        for char in num[1:]:
            while k and stack and char < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(char)
        if k:
            stack = stack[:-k]
        return str(int("".join(stack)))


solution = Solution()


num = "1432219"
k = 3
assert solution.removeKdigits(num, k) == "1219"

num = "10200"
k = 1
assert solution.removeKdigits(num, k) == "200"

num = "10"
k = 2
assert solution.removeKdigits(num, k) == "0"

num = "2111"
k = 2
assert solution.removeKdigits(num, k) == "11"

num = "111"
k = 2
assert solution.removeKdigits(num, k) == "1"

num = "10"
k = 1
assert solution.removeKdigits(num, k) == "0"

num = "12345"
k = 2
assert solution.removeKdigits(num, k) == "123"
