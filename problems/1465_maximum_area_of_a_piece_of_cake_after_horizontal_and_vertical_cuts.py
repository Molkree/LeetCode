# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts


class Solution:
    def maxArea(  # noqa: N802
        self, h: int, w: int, horizontal_cuts: list[int], vertical_cuts: list[int]
    ) -> int:
        row = 0
        heights = list[int]()
        for horizontal_cut in sorted(horizontal_cuts):
            heights.append(horizontal_cut - row)
            row = horizontal_cut
        heights.append(h - row)
        column = 0
        widths = list[int]()
        for vertical_cut in sorted(vertical_cuts):
            widths.append(vertical_cut - column)
            column = vertical_cut
        widths.append(w - column)
        return max(heights) * max(widths) % (10**9 + 7)


solution = Solution()


h = 5
w = 4
horizontal_cuts = [1, 2, 4]
vertical_cuts = [1, 3]
assert solution.maxArea(h, w, horizontal_cuts, vertical_cuts) == 4

h = 5
w = 4
horizontal_cuts = [3, 1]
vertical_cuts = [1]
assert solution.maxArea(h, w, horizontal_cuts, vertical_cuts) == 6

h = 5
w = 4
horizontal_cuts = [3]
vertical_cuts = [3]
assert solution.maxArea(h, w, horizontal_cuts, vertical_cuts) == 9

h = 1000000000
w = 1000000000
horizontal_cuts = [2]
vertical_cuts = [2]
assert solution.maxArea(h, w, horizontal_cuts, vertical_cuts) == 81
