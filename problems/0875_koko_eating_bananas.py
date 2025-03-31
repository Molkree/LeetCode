# https://leetcode.com/problems/koko-eating-bananas/
# 875. Koko Eating Bananas


from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:  # noqa: N802
        left = 1
        right = max(piles)
        while left != right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left


solution = Solution()


piles = [3, 6, 7, 11]
h = 8
assert solution.minEatingSpeed(piles, h) == 4

piles = [30, 11, 23, 4, 20]
h = 5
assert solution.minEatingSpeed(piles, h) == 30

piles = [30, 11, 23, 4, 20]
h = 6
assert solution.minEatingSpeed(piles, h) == 23
