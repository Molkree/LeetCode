# https://leetcode.com/problems/stream-of-characters/
# 1032. Stream of Characters


from collections import defaultdict
from functools import reduce
from typing import Any


class StreamChecker:
    def __init__(self, words: list[str]) -> None:
        def trie() -> defaultdict[str, Any]:
            return defaultdict(trie)

        self.trie = trie()
        for word in words:
            reduce(defaultdict[str, Any].__getitem__, word[::-1], self.trie)["#"] = True
        self.candidate = ""
        self.max_len = max(map(len, words))

    def query(self, letter: str) -> bool:
        self.candidate = (letter + self.candidate)[: self.max_len]
        node = self.trie
        for char in self.candidate:
            if char in node:
                node = node[char]
                if node["#"]:
                    return True
            else:
                break
        return False


stream_checker = StreamChecker(["cd", "f", "kl"])
assert not stream_checker.query("a")
assert not stream_checker.query("b")
assert not stream_checker.query("c")
assert stream_checker.query("d")
assert not stream_checker.query("e")
assert stream_checker.query("f")
assert not stream_checker.query("g")
assert not stream_checker.query("h")
assert not stream_checker.query("i")
assert not stream_checker.query("j")
assert not stream_checker.query("k")
assert stream_checker.query("l")
