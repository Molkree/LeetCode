# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 1249. Minimum Remove to Make Valid Parentheses


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:  # noqa: N802
        count = 0
        remove_right = list[int]()
        for ind, char in enumerate(s):
            if char == "(":
                count += 1
            elif char == ")":
                if count < 1:
                    remove_right.append(ind)
                else:
                    count -= 1
        remove_left = list[int]()
        ind = len(s) - 1
        while count:
            if s[ind] == "(":
                remove_left.append(ind)
                count -= 1
            ind -= 1
        remove_indices = remove_right + list(reversed(remove_left))
        new_s = ""
        ind = 0
        for stop in remove_indices:
            new_s += s[ind:stop]
            ind = stop + 1
        return new_s + s[ind:]


solution = Solution()


s = "))(("
assert solution.minRemoveToMakeValid(s) == ""
