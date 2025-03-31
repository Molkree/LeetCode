# https://leetcode.com/problems/clone-graph/
# 133. Clone Graph


from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:  # noqa: N802
        if not node:
            return None
        mapping = {node: Node(node.val)}
        stack = [node]
        while stack:
            next_node = stack.pop()
            for neighbor in next_node.neighbors:
                if neighbor not in mapping:
                    stack.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val)
                mapping[next_node].neighbors.append(mapping[neighbor])
        return mapping[node]


solution = Solution()


node_1 = Node(1)
node_2 = Node(2, [node_1])
node_3 = Node(3, [node_2])
node_1.neighbors = [node_2]
node_2.neighbors = [node_1, node_3]
clone = solution.cloneGraph(node_1)
