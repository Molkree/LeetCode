# https://leetcode.com/problems/non-overlapping-intervals/
# 435. Non-overlapping Intervals


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:  # noqa: N802
        intervals.sort(key=lambda x: x[1])
        count = 1
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                count += 1
                end = interval[1]
        return len(intervals) - count


solution = Solution()


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
assert solution.eraseOverlapIntervals(intervals) == 1

intervals = [[1, 2], [1, 2], [1, 2]]
assert solution.eraseOverlapIntervals(intervals) == 2

intervals = [[1, 2], [2, 3]]
assert solution.eraseOverlapIntervals(intervals) == 0

intervals = [[-65, -26], [-62, -49], [-40, -26]]
assert solution.eraseOverlapIntervals(intervals) == 1
