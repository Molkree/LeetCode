# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
# 1359. Count All Valid Pickup and Delivery Options


class Solution:
    def countOrders(self, n: int) -> int:  # noqa: N802
        result = 1
        modulo = 10**9 + 7
        for i in range(1, n + 1):
            result *= i * (2 * i - 1)
            result %= modulo
        return result


solution = Solution()


n = 1
assert solution.countOrders(n) == 1

n = 2
assert solution.countOrders(n) == 6

n = 3
assert solution.countOrders(n) == 90
