# https://leetcode.com/problems/search-suggestions-system/
# 1268. Search Suggestions System


from bisect import bisect_left


class Solution:
    def suggestedProducts(  # noqa: N802
        self, products: list[str], search_word: str
    ) -> list[list[str]]:
        result = list[list[str]]()
        products.sort()
        prefix = ""
        start = 0
        for char in search_word:
            prefix += char
            start += bisect_left(products[start:], prefix)
            result.append(list[str]())
            for i in range(3):
                suggestion_index = start + i
                if suggestion_index < len(products) and products[
                    suggestion_index
                ].startswith(prefix):
                    result[-1].append(products[suggestion_index])
        return result


solution = Solution()


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
search_word = "mouse"
assert solution.suggestedProducts(products, search_word) == [
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
]

products = ["havana"]
search_word = "havana"
assert solution.suggestedProducts(products, search_word) == [
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"],
    ["havana"],
]

products = ["bags", "baggage", "banner", "box", "cloths"]
search_word = "bags"
assert solution.suggestedProducts(products, search_word) == [
    ["baggage", "bags", "banner"],
    ["baggage", "bags", "banner"],
    ["baggage", "bags"],
    ["bags"],
]
