from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries):
        MX = 50000

        obstacles = SortedList([0, MX])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        bit = Fenwick(MX + 2)

        obs = list(obstacles)

        for i in range(1, len(obs)):
            gap = obs[i] - obs[i - 1]
            bit.update(obs[i] + 1, gap)

        ans = []

        for q in reversed(queries):

            if q[0] == 2:
                _, x, sz = q

                idx = obstacles.bisect_right(x)

                best = bit.query(x + 1)

                left = obstacles[idx - 1]
                best = max(best, x - left)

                ans.append(best >= sz)

            else:
                x = q[1]

                idx = obstacles.bisect_left(x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                obstacles.remove(x)

                bit.update(right + 1, right - left)

        return ans[::-1]