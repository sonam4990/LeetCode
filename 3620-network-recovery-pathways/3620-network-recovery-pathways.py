from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # your existing code
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        maxCost = 0

        for u, v, c in edges:
            graph[u].append((v, c))
            indegree[v] += 1
            maxCost = max(maxCost, c)

        # Topological Sort
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = 10 ** 30

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # Intermediate offline nodes are not allowed
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    nd = dist[u] + cost

                    if nd < dist[v]:
                        dist[v] = nd

            return dist[n - 1] <= k

        left = 0
        right = maxCost
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans