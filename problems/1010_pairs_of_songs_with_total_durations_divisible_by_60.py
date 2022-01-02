# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# 1010. Pairs of Songs With Total Durations Divisible by 60


class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:  # noqa: N802
        # first solution
        # remainders = sorted(map(lambda t: t % 60, time))

        # count = 0
        # pairs = dict[int, int]()
        # for song_len in remainders:
        #     if song_len not in pairs:
        #         pairs[song_len] = remainders.count((60 - song_len) % 60)
        #         if song_len in (0, 30) and pairs[song_len] > 0:
        #             pairs[song_len] -= 1
        #     count += pairs[song_len]

        # return count // 2
        # way simpler
        count = 0
        counter = [0] * 60
        for song_len in time:
            count += counter[-song_len % 60]
            counter[song_len % 60] += 1

        return count


solution = Solution()


time = [30, 20, 150, 100, 40]
assert solution.numPairsDivisibleBy60(time) == 3

time = [60, 60, 60]
assert solution.numPairsDivisibleBy60(time) == 3

time = [8, 8, 18, 42]
assert solution.numPairsDivisibleBy60(time) == 1

time = [21, 39, 21]
assert solution.numPairsDivisibleBy60(time) == 2
