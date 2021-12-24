# https://leetcode.com/problems/merge-intervals/
# 56. Merge Intervals


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        for next_start, next_end in intervals[1:]:
            end = result[-1][1]
            if next_start <= end:
                result[-1][1] = max(end, next_end)
            else:
                result.append([next_start, next_end])
        return result


solution = Solution()


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
assert solution.merge(intervals) == [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
assert solution.merge(intervals) == [[1, 5]]

intervals = [[1, 4], [0, 5]]
assert solution.merge(intervals) == [[0, 5]]
