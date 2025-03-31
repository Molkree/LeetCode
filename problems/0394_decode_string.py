# https://leetcode.com/problems/decode-string/
# 394. Decode String


class Solution:
    def decodeString(self, s: str) -> str:  # noqa: N802
        mult_stack = list[int]()
        str_stack = list[str]()
        result = ""
        multiplier = 0
        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == "[":
                str_stack.append(result)
                mult_stack.append(multiplier)
                result = ""
                multiplier = 0
            elif char == "]":
                prev_multiplier = mult_stack.pop()
                prev_result = str_stack.pop()
                result = prev_result + prev_multiplier * result
            else:
                result += char
        return result


solution = Solution()


s = "3[a]2[bc]"
assert solution.decodeString(s) == "aaabcbc"

s = "3[a2[c]]"
assert solution.decodeString(s) == "accaccacc"

s = "2[abc]3[cd]ef"
assert solution.decodeString(s) == "abcabccdcdcdef"

s = "abc3[cd]xyz"
assert solution.decodeString(s) == "abccdcdcdxyz"
