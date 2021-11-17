# https://leetcode.com/problems/maximize-distance-to-closest-person/
# 849. Maximize Distance to Closest Person


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:  # noqa: N802
        max_distance = 0
        empty_count = 0
        seen_seat = False
        for seat in seats:
            if seat:
                distance = (empty_count + 1) // 2 if seen_seat else empty_count
                max_distance = max(max_distance, distance)
                empty_count = 0
                seen_seat = True
            else:
                empty_count += 1
        if seats[-1] == 0:
            return max(max_distance, empty_count)
        return max_distance


solution = Solution()


seats = [1, 0, 0, 0, 1, 0, 1]
assert solution.maxDistToClosest(seats) == 2

seats = [1, 0, 0, 0]
assert solution.maxDistToClosest(seats) == 3

seats = [0, 1]
assert solution.maxDistToClosest(seats) == 1
