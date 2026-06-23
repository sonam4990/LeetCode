class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # length = 2
        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]

        if n == 2:
            return sum(up) + sum(down)

        for _ in range(3, n + 1):

            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for x in range(m):
                # sum of down[y] where y < x
                new_up[x] = pref_down[x]

                # sum of up[y] where y > x
                new_down[x] = (total_up - pref_up[x + 1]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD