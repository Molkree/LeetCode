# https://leetcode.com/problems/minimum-height-trees/
# 310. Minimum Height Trees


from collections import defaultdict


class Solution:
    def findMinHeightTrees(  # noqa: N802
        self, n: int, edges: list[list[int]]
    ) -> list[int]:
        if n <= 2:
            return list(range(n))

        neighbors: defaultdict[int, set[int]] = defaultdict(set[int])
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        leaves = [i for i in range(n) if len(neighbors[i]) == 1]
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves: list[int] = []
            while leaves:
                leaf = leaves.pop()
                inner_node = neighbors[leaf].pop()
                neighbors[inner_node].remove(leaf)
                if len(neighbors[inner_node]) == 1:
                    new_leaves.append(inner_node)
            leaves = new_leaves
        return leaves


solution = Solution()


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
assert sorted(solution.findMinHeightTrees(n, edges)) == sorted([1])

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
assert sorted(solution.findMinHeightTrees(n, edges)) == sorted([3, 4])

n = 1
edges: list[list[int]] = []
assert sorted(solution.findMinHeightTrees(n, edges)) == sorted([0])

n = 2
edges = [[0, 1]]
assert sorted(solution.findMinHeightTrees(n, edges)) == sorted([0, 1])
