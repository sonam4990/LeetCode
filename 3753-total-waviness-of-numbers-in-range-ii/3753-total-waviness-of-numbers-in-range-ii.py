from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1):
                # Returns: (count_of_numbers, total_waviness)
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # Still leading zeros
                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, 10, 10)
                        total_cnt += cnt
                        total_wav += wav

                    # First digit of the number
                    elif not started:
                        cnt, wav = dp(pos + 1, ntight, True, 10, d)
                        total_cnt += cnt
                        total_wav += wav

                    # Second digit of the number
                    elif prev2 == 10:
                        cnt, wav = dp(pos + 1, ntight, True, prev1, d)
                        total_cnt += cnt
                        total_wav += wav

                    # Third digit onwards
                    else:
                        extra = 0

                        if (prev1 > prev2 and prev1 > d) or \
                           (prev1 < prev2 and prev1 < d):
                            extra = 1

                        cnt, wav = dp(pos + 1, ntight, True, prev1, d)

                        total_cnt += cnt
                        total_wav += wav + extra * cnt

                return (total_cnt, total_wav)

            return dp(0, True, False, 10, 10)[1]

        return solve(num2) - solve(num1 - 1)