# https://leetcode.com/problems/implement-trie-prefix-tree/
# 208. Implement Trie (Prefix Tree)


class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {}
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:  # noqa: N802
        node = self
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


trie = Trie()
trie.insert("apple")
assert trie.search("apple")
assert not trie.search("app")
assert trie.startsWith("app")
trie.insert("app")
assert trie.search("app")
