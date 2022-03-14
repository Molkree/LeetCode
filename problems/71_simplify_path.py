# https://leetcode.com/problems/simplify-path/
# 71. Simplify Path


import os


class Solution:
    def simplifyPath(self, path: str) -> str:  # noqa: N802
        # replace is needed on Windows
        return os.path.normpath(path).replace("\\", "/")
        # custom solution
        dirs = path.split("/")
        stack = list[str]()
        for dir in dirs:
            if dir:
                if dir == "..":
                    if stack:
                        stack.pop()
                elif dir != ".":
                    stack.append(dir)
        return "/" + "/".join(stack)


solution = Solution()


path = "/home/"
assert solution.simplifyPath(path) == "/home"

path = "/../"
assert solution.simplifyPath(path) == "/"

path = "/home//foo/"
assert solution.simplifyPath(path) == "/home/foo"

path = "/path/../"
assert solution.simplifyPath(path) == "/"
