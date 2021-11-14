# https://leetcode.com/problems/iterator-for-combination/
# 1286. Iterator for Combination


class CombinationIterator:
    def gen_combinations(self, characters: str, combination_length: int) -> list[str]:
        if combination_length == 1:
            return list(characters)
        result: list[str] = []
        for ind, character in enumerate(characters[: 1 - combination_length]):
            result += [
                character + string
                for string in self.gen_combinations(
                    characters[ind + 1 :], combination_length - 1
                )
            ]
        return result

    def __init__(self, characters: str, combination_length: int):
        self.combinations = self.gen_combinations(characters, combination_length)
        self.current_index = 0

    def next(self) -> str:
        self.current_index += 1
        return self.combinations[self.current_index - 1]

    def hasNext(self) -> bool:  # noqa: N802
        return self.current_index < len(self.combinations)


itr = CombinationIterator("abc", 2)
assert itr.next() == "ab"
assert itr.hasNext()
assert itr.next() == "ac"
assert itr.hasNext()
assert itr.next() == "bc"
assert not itr.hasNext()

itr = CombinationIterator("abc", 1)
assert itr.next() == "a"
assert itr.hasNext()
assert itr.next() == "b"
assert itr.hasNext()
assert itr.next() == "c"
assert not itr.hasNext()

itr = CombinationIterator("abc", 3)
assert itr.next() == "abc"
assert not itr.hasNext()

itr = CombinationIterator("abcd", 2)
assert itr.next() == "ab"
assert itr.hasNext()
assert itr.next() == "ac"
assert itr.hasNext()
assert itr.next() == "ad"
assert itr.hasNext()
assert itr.next() == "bc"
assert itr.hasNext()
assert itr.next() == "bd"
assert itr.hasNext()
assert itr.next() == "cd"
assert not itr.hasNext()
