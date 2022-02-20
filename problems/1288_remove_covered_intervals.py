# https://leetcode.com/problems/remove-covered-intervals/
# 1288. Remove Covered Intervals


class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:  # noqa: N802
        # O(n * logn)
        intervals.sort()
        non_overlapping_intervals = [intervals[0]]
        for interval in intervals:
            last_interval = non_overlapping_intervals[-1]
            if interval[0] == last_interval[0] and last_interval[1] < interval[1]:
                non_overlapping_intervals[-1] = interval
            elif last_interval[0] < interval[0] and last_interval[1] < interval[1]:
                non_overlapping_intervals.append(interval)
        return len(non_overlapping_intervals)
        # O(n ^ 2)
        good_intervals = list[list[int]]()
        for interval in intervals:
            overlapped = False
            for other_interval in intervals:
                if (
                    other_interval != interval
                    and other_interval[0] <= interval[0]
                    and interval[1] <= other_interval[1]
                ):
                    overlapped = True
                    break
            if not overlapped:
                good_intervals.append(interval)
        return len(good_intervals)


solution = Solution()


intervals = [[1, 4], [5, 6], [3, 4], [4, 8]]
assert solution.removeCoveredIntervals(intervals) == 2

intervals = [[1, 4], [3, 6], [2, 8]]
assert solution.removeCoveredIntervals(intervals) == 2

intervals = [[1, 4], [2, 3]]
assert solution.removeCoveredIntervals(intervals) == 1

intervals = [[1, 2], [1, 4], [3, 4]]
assert solution.removeCoveredIntervals(intervals) == 1
