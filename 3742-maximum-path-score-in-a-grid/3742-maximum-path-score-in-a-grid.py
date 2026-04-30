from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])

        NEG = -10**9

        # dp[i][j][cost]
        dp = [[[NEG] * (k + 1) for _ in range(n)] for _ in range(m)]

        # starting point
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):

                for cost in range(k + 1):

                    if dp[i][j][cost] == NEG:
                        continue

                    # move down
                    if i + 1 < m:

                        val = grid[i + 1][j]

                        new_cost = cost + (1 if val != 0 else 0)

                        if new_cost <= k:

                            dp[i + 1][j][new_cost] = max(
                                dp[i + 1][j][new_cost],
                                dp[i][j][cost] + val
                            )

                    # move right
                    if j + 1 < n:

                        val = grid[i][j + 1]

                        new_cost = cost + (1 if val != 0 else 0)

                        if new_cost <= k:

                            dp[i][j + 1][new_cost] = max(
                                dp[i][j + 1][new_cost],
                                dp[i][j][cost] + val
                            )

        ans = max(dp[m - 1][n - 1])

        return ans if ans != NEG else -1