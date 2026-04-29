from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Only one column -> no horizontal neighbor possible
        if n == 1:
            return 0

        # prefix[col][r]
        # sum of grid[0:r][col]
        prefix = [[0] * (n + 1) for _ in range(n)]

        for col in range(n):
            for row in range(n):
                prefix[col][row + 1] = prefix[col][row] + grid[row][col]

        # gain if current column has black depth = cur
        # and at least one neighbor has black depth = mx
        #
        # black depth means:
        # first `depth` cells are black
        #
        # white rows are [cur ... n-1]
        # contributing rows are [cur ... mx-1]
        def gain(col, cur, mx):
            if mx <= cur:
                return 0
            return prefix[col][mx] - prefix[col][cur]

        B = n + 1
        NEG = -10**18

        # dp[prev][curr]
        #
        # prev = black depth of column i-1
        # curr = black depth of column i
        #
        # value = best score processed so far

        dp = [[NEG] * B for _ in range(B)]

        # initialize using column 0 contribution
        # left neighbor outside grid => depth 0
        for b0 in range(B):
            for b1 in range(B):
                dp[b0][b1] = gain(0, b0, b1)

        # process middle columns
        for col in range(1, n - 1):

            new_dp = [[NEG] * B for _ in range(B)]

            for curr in range(B):

                # best prefix:
                # max(dp[p][curr]) for p <= t
                best_prefix = [NEG] * B

                best = NEG
                for p in range(B):
                    best = max(best, dp[p][curr])
                    best_prefix[p] = best

                # best suffix:
                # max(dp[p][curr] + gain(col,curr,p))
                best_suffix = [NEG] * (B + 1)

                best = NEG
                for p in range(B - 1, -1, -1):
                    best = max(best,
                               dp[p][curr] + gain(col, curr, p))
                    best_suffix[p] = best

                for nxt in range(B):

                    # case 1:
                    # prev <= nxt
                    option1 = best_prefix[nxt] + gain(col, curr, nxt)

                    # case 2:
                    # prev > nxt
                    option2 = best_suffix[nxt + 1]

                    new_dp[curr][nxt] = max(option1, option2)

            dp = new_dp

        # finalize last column
        ans = 0
        last = n - 1

        for prev in range(B):
            for curr in range(B):

                # right outside grid => depth 0
                total = dp[prev][curr] + gain(last, curr, prev)

                ans = max(ans, total)

        return ans