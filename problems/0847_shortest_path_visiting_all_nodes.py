# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# 847. Shortest Path Visiting All Nodes


class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:  # noqa: N802
        graph_len = len(graph)
        state_cache = dict[tuple[int, int], int]()

        def dp(node: int, mask: int) -> int:
            state = node, mask
            if state in state_cache:
                return state_cache[state]
            if mask & (mask - 1) == 0:  # one node visited
                return 0
            state_cache[state] = 100  # mask len is 20 for 12 node graph?
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    visited = 1 + dp(neighbor, mask)
                    not_visited = 1 + dp(neighbor, mask ^ (1 << node))
                    state_cache[state] = min(state_cache[state], visited, not_visited)
            return state_cache[state]

        ending_mask = (1 << graph_len) - 1
        return min(dp(node, ending_mask) for node in range(graph_len))


solution = Solution()


graph = [[1, 2, 3], [0], [0], [0]]
assert solution.shortestPathLength(graph) == 4

graph = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
assert solution.shortestPathLength(graph) == 4
