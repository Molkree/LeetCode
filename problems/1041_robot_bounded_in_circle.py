# https://leetcode.com/problems/robot-bounded-in-circle/
# 1041. Robot Bounded In Circle


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:  # noqa: N802
        move = {
            "L": {"U": "L", "L": "D", "D": "R", "R": "U"},
            "R": {"U": "R", "R": "D", "D": "L", "L": "U"},
        }
        moves = {"U": 0, "L": 0, "D": 0, "R": 0}
        direction = "U"
        for instruction in instructions:
            if instruction in "LR":
                direction = move[instruction][direction]
            else:
                moves[direction] += 1
        return direction != "U" or moves["U"] == moves["D"] and moves["L"] == moves["R"]


solution = Solution()


instructions = "GGLLGG"
assert solution.isRobotBounded(instructions)

instructions = "GG"
assert not solution.isRobotBounded(instructions)

instructions = "GL"
assert solution.isRobotBounded(instructions)

instructions = "LLGRL"
assert solution.isRobotBounded(instructions)
