# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# 1178. Number of Valid Words for Each Puzzle


class Solution:
    def findNumOfValidWords(  # noqa: N802
        self, words: list[str], puzzles: list[str]
    ) -> list[int]:
        def str_to_bitmask(word: str) -> int:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord("a"))
            return bitmask

        word_bins: dict[int, int] = {}
        for word in words:
            bitmask = str_to_bitmask(word)
            if bitmask not in word_bins:
                word_bins[bitmask] = 1
            else:
                word_bins[bitmask] += 1
        result: list[int] = []
        for puzzle in puzzles:
            bitmask = str_to_bitmask(puzzle)
            first_char_bit_pos = ord(puzzle[0]) - ord("a")
            subset = bitmask
            count = 0
            while subset > 0:
                if subset >> first_char_bit_pos & 1 and subset in word_bins:
                    count += word_bins[subset]
                subset = (subset - 1) & bitmask
            result.append(count)
        return result


solution = Solution()


words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
assert solution.findNumOfValidWords(words, puzzles) == [1, 1, 3, 2, 4, 0]

words = ["apple", "pleas"]
puzzles = ["aelpsxy"]
assert solution.findNumOfValidWords(words, puzzles) == [2]

words = ["apple", "pleas", "please"]
puzzles = ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]
assert solution.findNumOfValidWords(words, puzzles) == [0, 1, 3, 2, 0]

words = ["pleas", "please"]
puzzles = ["aelpsxy"]
assert solution.findNumOfValidWords(words, puzzles) == [2]
