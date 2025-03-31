# https://leetcode.com/problems/encode-and-decode-tinyurl/
# 535. Encode and Decode TinyURL


import hashlib


class Codec:
    db = dict[str, str]()

    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL."""
        short_url = hashlib.shake_256(long_url.encode()).hexdigest(8)
        self.db[short_url] = long_url
        return short_url

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.db[short_url]
