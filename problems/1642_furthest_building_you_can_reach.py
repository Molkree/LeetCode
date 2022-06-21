# https://leetcode.com/problems/furthest-building-you-can-reach/
# 1642. Furthest Building You Can Reach


import heapq


class Solution:
    def furthestBuilding(  # noqa: N802
        self, heights: list[int], bricks: int, ladders: int
    ) -> int:
        building = 0
        ladder_jumps = list[int]()
        while building < len(heights) - 1:
            diff_height = heights[building + 1] - heights[building]
            if len(ladder_jumps) < ladders:
                heapq.heappush(ladder_jumps, diff_height)
            else:
                if (need_bricks := heapq.heappushpop(ladder_jumps, diff_height)) > 0:
                    bricks -= need_bricks
            if bricks < 0:
                break
            building += 1
        return building


solution = Solution()


heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1
assert solution.furthestBuilding(heights, bricks, ladders) == 4

heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
bricks = 10
ladders = 2
assert solution.furthestBuilding(heights, bricks, ladders) == 7

heights = [14, 3, 19, 3]
bricks = 17
ladders = 0
assert solution.furthestBuilding(heights, bricks, ladders) == 3

heights = [7, 5, 13]
bricks = 0
ladders = 0
assert solution.furthestBuilding(heights, bricks, ladders) == 1

heights = [7, 5, 13]
bricks = 0
ladders = 5
assert solution.furthestBuilding(heights, bricks, ladders) == 2
