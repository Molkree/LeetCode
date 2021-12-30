# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# 1015. Smallest Integer Divisible by K


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:  # noqa: N802
        # fast
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1
        # slower
        # slow, fast, length = 0, 0, 0
        # while True:
        #     slow = (slow * 10 + 1) % k
        #     fast = ((fast * 10 + 1) % k * 10 + 1) % k
        #     length += 1
        #     if slow == 0:
        #         return length
        #     if slow == fast:
        #         return -1


solution = Solution()


k = 1
assert solution.smallestRepunitDivByK(k) == 1

k = 2
assert solution.smallestRepunitDivByK(k) == -1

k = 3
assert solution.smallestRepunitDivByK(k) == 3
