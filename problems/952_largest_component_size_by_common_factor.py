# https://leetcode.com/problems/largest-component-size-by-common-factor/
# 952. Largest Component Size by Common Factor


from collections import Counter, defaultdict
from math import sqrt


class DSU:
    def __init__(self, n: int) -> None:
        self.values = list(range(n))

    def find(self, x: int):
        if self.values[x] != x:
            self.values[x] = self.find(self.values[x])
        return self.values[x]

    def union(self, x: int, y: int):
        xr, yr = self.find(x), self.find(y)
        self.values[xr] = yr


class Solution:
    def primes_set(self, n: int) -> set[int]:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | {i}
        return {n}

    def largestComponentSize(self, nums: list[int]) -> int:  # noqa: N802
        n = len(nums)
        dsu = DSU(n)
        primes: defaultdict[int, list[int]] = defaultdict(list)
        for i, num in enumerate(nums):
            primes_set = self.primes_set(num)
            for prime in primes_set:
                primes[prime].append(i)

        for indexes in primes.values():
            for i in range(len(indexes) - 1):
                dsu.union(indexes[i], indexes[i + 1])

        return max(Counter(dsu.find(i) for i in range(n)).values())


solution = Solution()


nums = [4, 6, 15, 35]
assert solution.largestComponentSize(nums) == 4

nums = [20, 50, 9, 63]
assert solution.largestComponentSize(nums) == 2

nums = [2, 3, 6, 7, 4, 12, 21, 39]
assert solution.largestComponentSize(nums) == 8
