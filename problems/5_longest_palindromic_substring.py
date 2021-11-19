# https://leetcode.com/problems/longest-palindromic-substring/
# 5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:  # noqa: N802
        def is_palindrome(s: str) -> bool:
            if len(s) == 1:
                return True
            middle = len(s) // 2
            return s[:middle] == s[-1 : -1 - middle : -1]

        max_len = 0
        max_palindrome = s[0]
        for i in range(len(s)):
            if len(s) - i < max_len:
                return max_palindrome
            for j in range(len(s), i, -1):
                if is_palindrome(s[i:j]) and j - i >= max_len:
                    max_len = j - i
                    max_palindrome = s[i:j]
        return max_palindrome


solution = Solution()


s = "cbbd"
assert solution.longestPalindrome(s) == "bb"

s = "a"
assert solution.longestPalindrome(s) == "a"

s = "ac"
assert solution.longestPalindrome(s) in ("a", "c")

s = "babad"
assert solution.longestPalindrome(s) in ("bab", "aba")

s = "bb"
assert solution.longestPalindrome(s) == "bb"

s = "dwvvlmokkdtnbrpnueyamqwrvrcwpwiaglvoizmsfuxzgvkvsexgwxwoygayznjlswucmoehugrkjkduwtdrguaqtqwdvrekxgphbitvxmpazkceodsyjzuvjfvgjbtiawrpcwomeiwgoelilfylydsdgawybjjmbgfhkndnvqdryncglaxmzndsoziqqmrwticjomsyatisjduifwfzjkgpdpneurlylzgrdlixhosmmwhaqgpxhmjqxsasfnqnppyufxwpukaruvlnfetymzqwzfklpwdwwrupvrttxdkgjbrzwuvwkkjiynnoemfzrjaepvejvxqkvhqtegtiwtbwlneqzryjzzjyrzqenlwbtwitgetqhvkqxvjevpeajrzfmeonnyijkkwvuwzrbjgkdxttrvpurwwdwplkfzwqzmytefnlvurakupwxfuyppnqnfsasxqjmhxpgqahwmmsohxildrgzlylruenpdpgkjzfwfiudjsitaysmojcitwrmqqizosdnzmxalgcnyrdqvndnkhfgbmjjbywagdsdylyflileogwiemowcprwaitbjgvfjvuzjysdoeckzapmxvtibhpgxkervdwqtqaugrdtwudkjkrguheomcuwsljnzyagyowxwgxesvkvgzxufsmziovlgaiwpwcrvrwqmayeunprbntdkkomlvvwd"
print(solution.longestPalindrome(s))
