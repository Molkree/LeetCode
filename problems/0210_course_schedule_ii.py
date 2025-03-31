# https://leetcode.com/problems/course-schedule-ii/
# 210. Course Schedule II


from collections import defaultdict


class Solution:
    def findOrder(  # noqa: N802
        self, num_courses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        neighbours = defaultdict[int, set[int]](set[int])
        for start, end in prerequisites:
            neighbours[start].add(end)
        todo = [False] * num_courses
        done = [False] * num_courses
        path = list[int]()

        def acyclic(course: int) -> bool:
            if todo[course]:
                return False
            if done[course]:
                return True
            todo[course] = True
            done[course] = True
            for prereq in neighbours[course]:
                if not acyclic(prereq):
                    return False
            todo[course] = False
            path.append(course)
            return True

        for course in range(num_courses):
            if not done[course] and not acyclic(course):
                return []
        return path


solution = Solution()


num_courses = 2
prerequisites = [[1, 0]]
assert solution.findOrder(num_courses, prerequisites) in ([0, 1],)

num_courses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
assert solution.findOrder(num_courses, prerequisites) in ([0, 1, 2, 3], [0, 2, 1, 3])

num_courses = 1
prerequisites: list[list[int]] = []
assert solution.findOrder(num_courses, prerequisites) in ([0],)

num_courses = 2
prerequisites: list[list[int]] = [[1, 0], [0, 1]]
assert solution.findOrder(num_courses, prerequisites) in ([],)

num_courses = 3
prerequisites: list[list[int]] = [[1, 0]]
assert solution.findOrder(num_courses, prerequisites) in ([0, 1, 2], [2, 0, 1])

num_courses = 2
prerequisites: list[list[int]] = []
assert solution.findOrder(num_courses, prerequisites) in ([1, 0], [0, 1])
