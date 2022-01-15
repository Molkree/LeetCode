# https://leetcode.com/problems/jump-game-iv/
# 1345. Jump Game IV


from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:  # noqa: N802
        graph = defaultdict[int, list[int]](list)
        for ind, num in enumerate(arr):
            graph[num].append(ind)
        visited = set[int]()
        queue = deque[tuple[int, int]]([(0, 0)])
        while queue:
            ind, dist = queue.popleft()
            visited.add(ind)
            if ind == len(arr) - 1:
                return dist
            for neighbor in graph[arr[ind]] + [ind - 1, ind + 1]:
                if neighbor not in visited and 0 <= neighbor < len(arr):
                    queue.append((neighbor, dist + 1))
            graph[arr[ind]].clear()
        return -1


solution = Solution()


arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
assert solution.minJumps(arr) == 3

arr = [7]
assert solution.minJumps(arr) == 0

arr = [7, 6, 9, 6, 9, 6, 9, 7]
assert solution.minJumps(arr) == 1
