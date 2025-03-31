# https://leetcode.com/problems/find-the-town-judge/
# 997. Find the Town Judge


from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:  # noqa: N802
        if not trust and n == 1:
            return 1
        candidates = defaultdict[int, int](int)
        for source, target in trust:
            if candidates[target] != -1:
                candidates[target] += 1
            candidates[source] = -1
        judge = 1
        for judge, people in candidates.items():
            if people == n - 1:
                return judge
        return -1


solution = Solution()


n = 2
trust = [[1, 2]]
assert solution.findJudge(n, trust) == 2

n = 3
trust = [[1, 3], [2, 3]]
assert solution.findJudge(n, trust) == 3

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
assert solution.findJudge(n, trust) == -1

n = 1
trust = list[list[int]]()
assert solution.findJudge(n, trust) == 1

n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
assert solution.findJudge(n, trust) == 3

n = 2
trust = [[1, 2], [2, 1]]
assert solution.findJudge(n, trust) == -1

n = 2
trust = list[list[int]]()
assert solution.findJudge(n, trust) == -1
