# https://leetcode.com/problems/matchsticks-to-square/
# 473. Matchsticks to Square


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_sum = sum(matchsticks)
        subset_target = total_sum // 4
        if subset_target * 4 != total_sum:
            return False

        visited = [False] * len(matchsticks)
        matchsticks.sort(reverse=True)

        def can_partition(k: int, current_sum: int = 0, ind: int = 0) -> bool:
            if k == 1:
                return True
            if current_sum == subset_target:
                return can_partition(k - 1)
            for i in range(ind, len(matchsticks)):
                if not visited[i] and current_sum + matchsticks[i] <= subset_target:
                    visited[i] = True
                    if can_partition(k, current_sum + matchsticks[i], i + 1):
                        return True
                    visited[i] = False
            return False

        return can_partition(4)


solution = Solution()


matchsticks = [1, 1, 2, 2, 2]
assert solution.makesquare(matchsticks)

matchsticks = [3, 3, 3, 3, 4]
assert not solution.makesquare(matchsticks)
