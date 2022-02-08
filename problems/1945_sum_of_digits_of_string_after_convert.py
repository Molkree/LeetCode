# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# 1945. Sum of Digits of String After Convert


class Solution:
    def getLucky(self, s: str, k: int) -> int:  # noqa: N802
        s = "".join(map(lambda char: str(ord(char) - ord("a") + 1), s))
        num = int(s)
        for _ in range(k):
            num = sum(map(int, str(num)))
        return num


solution = Solution()


s = "zbax"
k = 2
assert solution.getLucky(s, k) == 8

s = "iiii"
k = 1
assert solution.getLucky(s, k) == 36

s = "leetcode"
k = 2
assert solution.getLucky(s, k) == 6
