from heapq import heappush, heappop
from math import log2

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        LOG = (n).bit_length()

        stMax = [[0] * LOG for _ in range(n)]
        stMin = [[0] * LOG for _ in range(n)]

        for i in range(n):
            stMax[i][0] = nums[i]
            stMin[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                stMax[i][j] = max(
                    stMax[i][j - 1],
                    stMax[i + half][j - 1]
                )

                stMin[i][j] = min(
                    stMin[i][j - 1],
                    stMin[i + half][j - 1]
                )

            j += 1

        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1

        def getValue(l, r):
            j = logs[r - l + 1]

            mx = max(
                stMax[l][j],
                stMax[r - (1 << j) + 1][j]
            )

            mn = min(
                stMin[l][j],
                stMin[r - (1 << j) + 1][j]
            )

            return mx - mn

        heap = []

        for l in range(n):
            val = getValue(l, n - 1)
            heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heappop(heap)

            ans += -val

            if r > l:
                nxt = getValue(l, r - 1)
                heappush(heap, (-nxt, l, r - 1))

        return ans