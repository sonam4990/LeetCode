from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def calc(n):
            if n < 0:
                return 0

            digits = str(n)

            @lru_cache(None)
            def dfs(pos, tight, started, prev2, prev1):
                if pos == len(digits):
                    return (1, 0)  # (count_numbers, total_waviness)

                limit = int(digits[pos]) if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dfs(pos + 1, ntight, False, 10, 10)
                        total_count += cnt
                        total_waviness += wav

                    elif not started:
                        cnt, wav = dfs(pos + 1, ntight, True, 10, d)
                        total_count += cnt
                        total_waviness += wav

                    elif prev2 == 10:
                        cnt, wav = dfs(pos + 1, ntight, True, prev1, d)
                        total_count += cnt
                        total_waviness += wav

                    else:
                        extra = int(
                            (prev1 > prev2 and prev1 > d) or
                            (prev1 < prev2 and prev1 < d)
                        )

                        cnt, wav = dfs(pos + 1, ntight, True, prev1, d)

                        total_count += cnt
                        total_waviness += wav + extra * cnt

                return total_count, total_waviness

            return dfs(0, True, False, 10, 10)[1]

        return calc(num2) - calc(num1 - 1)