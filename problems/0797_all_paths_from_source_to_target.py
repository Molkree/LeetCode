# https://leetcode.com/problems/all-paths-from-source-to-target/
# 797. All Paths From Source to Target


class Solution:
    def allPathsSourceTarget(  # noqa: N802
        self, graph: list[list[int]]
    ) -> list[list[int]]:
        paths: list[list[int]] = []
        stack: list[list[int]] = [[0, node] for node in graph[0]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == len(graph) - 1:
                paths.append(path)
            else:
                for neighbor in graph[node]:
                    stack.append(path + [neighbor])
        return paths


solution = Solution()


graph = [[1, 2], [3], [3], []]
assert sorted(solution.allPathsSourceTarget(graph)) == sorted([[0, 1, 3], [0, 2, 3]])

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
assert sorted(solution.allPathsSourceTarget(graph)) == sorted(
    [
        [0, 4],
        [0, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 4],
    ]
)

graph = [[1], []]
assert sorted(solution.allPathsSourceTarget(graph)) == sorted([[0, 1]])

graph = [[1, 2, 3], [2], [3], []]
assert sorted(solution.allPathsSourceTarget(graph)) == sorted(
    [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
)

graph = [[1, 3], [2], [3], []]
assert sorted(solution.allPathsSourceTarget(graph)) == sorted([[0, 1, 2, 3], [0, 3]])
