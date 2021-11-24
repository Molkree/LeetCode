# https://leetcode.com/problems/interval-list-intersections/
# 986. Interval List Intersections


class Solution:
    def intervalIntersection(  # noqa: N802
        self, first_list: list[list[int]], second_list: list[list[int]]
    ) -> list[list[int]]:
        # my initial clunky solution
        # if not first_list or not second_list:
        #     return []
        # intersections: list[list[int]] = []
        # second_index = 0
        # for first_start, first_end in first_list:
        #     second_start, second_end = second_list[second_index]
        #     while second_end < first_start:
        #         second_index += 1
        #         if second_index == len(second_list):
        #             return intersections
        #         second_start, second_end = second_list[second_index]
        #     if second_start <= first_start <= first_end:
        #         intersections.append([first_start, min(first_end, second_end)])
        #         if second_end <= first_end:
        #             second_index += 1
        #             if second_index == len(second_list):
        #                 return intersections
        #             second_start, second_end = second_list[second_index]
        #     while first_start <= second_start and second_end <= first_end:
        #         intersections.append([second_start, second_end])
        #         second_index += 1
        #         if second_index == len(second_list):
        #             return intersections
        #         second_start, second_end = second_list[second_index]
        #     if first_start < second_start <= first_end:
        #         intersections.append([second_start, first_end])
        # return intersections
        # shorter and easier solution
        intersections: list[list[int]] = []
        first_index = second_index = 0
        while first_index < len(first_list) and second_index < len(second_list):
            first_start, first_end = first_list[first_index]
            second_start, second_end = second_list[second_index]
            intersection_start = max(first_start, second_start)
            intersection_end = min(first_end, second_end)
            if intersection_start <= intersection_end:
                intersections.append([intersection_start, intersection_end])
            if first_end < second_end:
                first_index += 1
            else:
                second_index += 1
        return intersections


solution = Solution()


first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
assert solution.intervalIntersection(first_list, second_list) == [
    [1, 2],
    [5, 5],
    [8, 10],
    [15, 23],
    [24, 24],
    [25, 25],
]

first_list = [[1, 3], [5, 9]]
second_list: list[list[int]] = []
assert solution.intervalIntersection(first_list, second_list) == []

first_list: list[list[int]] = []
second_list = [[4, 8], [10, 12]]
assert solution.intervalIntersection(first_list, second_list) == []

first_list = [[1, 7]]
second_list = [[3, 10]]
assert solution.intervalIntersection(first_list, second_list) == [[3, 7]]

first_list = [[3, 10]]
second_list = [[5, 10]]
assert solution.intervalIntersection(first_list, second_list) == [[5, 10]]

first_list = [[0, 4], [7, 8], [12, 19]]
second_list = [[0, 10], [14, 15], [18, 20]]
assert solution.intervalIntersection(first_list, second_list) == [
    [0, 4],
    [7, 8],
    [14, 15],
    [18, 19],
]
