# https://leetcode.com/problems/happy-number/
# 202. Happy Number


class Solution:
    def isHappy(self, n: int) -> bool:  # noqa: N802
        visited: set[int] = set()
        visited.add(n)
        while n != 1:
            sum = 0
            while n:
                n, digit = divmod(n, 10)
                sum += digit * digit
            if sum in visited:
                return False
            n = sum
            visited.add(n)
        return True


solution = Solution()


n = 19
assert solution.isHappy(n)

n = 2
assert not solution.isHappy(n)

n = 1
assert solution.isHappy(n)
