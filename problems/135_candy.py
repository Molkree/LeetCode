# https://leetcode.com/problems/candy/
# 135. Candy


class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)
        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)
        return sum(candies)


solution = Solution()


ratings = [1, 0, 2]
assert solution.candy(ratings) == 5

ratings = [1, 2, 2]
assert solution.candy(ratings) == 4

ratings = [2, 1, 0]
assert solution.candy(ratings) == 6
