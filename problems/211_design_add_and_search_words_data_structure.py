# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# 211. Design Add and Search Words Data Structure


class WordDictionary:
    class Trie:
        def __init__(self) -> None:
            self.children = dict[str, WordDictionary.Trie]()
            self.is_word = False

        def insert(self, word: str) -> None:
            node = self
            for char in word:
                if char not in node.children:
                    node.children[char] = WordDictionary.Trie()
                node = node.children[char]
            node.is_word = True

        def search(self, word: str) -> bool:
            node = self
            for i, char in enumerate(word):
                if char == ".":
                    return any(
                        child.search(word[i + 1 :]) for child in node.children.values()
                    )
                if char in node.children:
                    node = node.children[char]
                else:
                    return False
            return node.is_word

    def __init__(self) -> None:
        self.trie = self.Trie()

    def addWord(self, word: str) -> None:  # noqa: N802
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")
assert not word_dictionary.search("pad")
assert word_dictionary.search("bad")
assert word_dictionary.search(".ad")
assert word_dictionary.search("b..")
