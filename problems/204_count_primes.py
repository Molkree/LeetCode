# https://leetcode.com/problems/count-primes/
# 204. Count Primes


class Solution:
    def countPrimes(self, n: int) -> int:  # noqa: N802
        is_prime = [True] * n
        candidate = 2
        while candidate * candidate < n:
            if not is_prime[candidate]:
                candidate += 1
                continue
            for composite in range(candidate * candidate, n, candidate):
                is_prime[composite] = False
            candidate += 1
        return is_prime[2:].count(True)


solution = Solution()


n = 10
assert solution.countPrimes(n) == 4

n = 0
assert solution.countPrimes(n) == 0

n = 1
assert solution.countPrimes(n) == 0

n = 688843
assert solution.countPrimes(n) == 55725
