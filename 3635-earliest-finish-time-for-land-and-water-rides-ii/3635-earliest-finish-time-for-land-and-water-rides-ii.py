from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        ans = inf

        # ---------- Land -> Water ----------

        water = sorted(
            zip(waterStartTime, waterDuration)
        )

        starts = [s for s, d in water]

        prefMinDur = []
        cur = inf

        for s, d in water:
            cur = min(cur, d)
            prefMinDur.append(cur)

        suffMinFinish = [0] * len(water)

        cur = inf

        for i in range(len(water) - 1, -1, -1):
            cur = min(cur, water[i][0] + water[i][1])
            suffMinFinish[i] = cur

        for s, d in zip(landStartTime, landDuration):

            finishLand = s + d

            idx = bisect_right(starts, finishLand)

            if idx > 0:
                ans = min(
                    ans,
                    finishLand + prefMinDur[idx - 1]
                )

            if idx < len(water):
                ans = min(
                    ans,
                    suffMinFinish[idx]
                )

        # ---------- Water -> Land ----------

        land = sorted(
            zip(landStartTime, landDuration)
        )

        starts = [s for s, d in land]

        prefMinDur = []
        cur = inf

        for s, d in land:
            cur = min(cur, d)
            prefMinDur.append(cur)

        suffMinFinish = [0] * len(land)

        cur = inf

        for i in range(len(land) - 1, -1, -1):
            cur = min(cur, land[i][0] + land[i][1])
            suffMinFinish[i] = cur

        for s, d in zip(waterStartTime, waterDuration):

            finishWater = s + d

            idx = bisect_right(starts, finishWater)

            if idx > 0:
                ans = min(
                    ans,
                    finishWater + prefMinDur[idx - 1]
                )

            if idx < len(land):
                ans = min(
                    ans,
                    suffMinFinish[idx]
                )

        return ans