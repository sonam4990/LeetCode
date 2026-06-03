class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        ans = float('inf')

        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            for j in range(m):

                # Land -> Water
                land_finish = landStartTime[i] + landDuration[i]

                finish1 = max(
                    land_finish,
                    waterStartTime[j]
                ) + waterDuration[j]

                ans = min(ans, finish1)

                # Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]

                finish2 = max(
                    water_finish,
                    landStartTime[i]
                ) + landDuration[i]

                ans = min(ans, finish2)

        return ans