# https://leetcode.com/problems/can-place-flowers/
# 605. Can Place Flowers


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:  # noqa: N802
        if len(flowerbed) < 3:
            return not (any(flowerbed) and n > 0 or n > 1)
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            n -= 1
            flowerbed[-1] = 1
        return n <= 0


solution = Solution()


flowerbed = [1, 0, 0, 0, 1]
n = 1
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [1, 0, 0, 0, 1]
n = 2
assert not solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0]
n = 1
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [1]
n = 1
assert not solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 0]
n = 1
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 0]
n = 2
assert not solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 0, 0]
n = 1
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 0, 0]
n = 2
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 0, 0, 0]
n = 2
assert solution.canPlaceFlowers(flowerbed, n)

flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
assert not solution.canPlaceFlowers(flowerbed, n)

flowerbed = [0, 1, 0]
n = 1
assert not solution.canPlaceFlowers(flowerbed, n)
