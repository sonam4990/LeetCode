from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)

        # ---------- Prime Check ----------
        def is_prime(x):

            if x < 2:
                return False

            i = 2

            while i * i <= x:

                if x % i == 0:
                    return False

                i += 1

            return True

        # ---------- Build Factor Map ----------
        factor_map = defaultdict(list)

        for i, num in enumerate(nums):

            x = num
            d = 2

            while d * d <= x:

                if x % d == 0:

                    factor_map[d].append(i)

                    while x % d == 0:
                        x //= d

                d += 1

            if x > 1:
                factor_map[x].append(i)

        # ---------- BFS ----------
        q = deque([0])

        visited = [False] * n
        visited[0] = True

        used_prime = set()

        steps = 0

        while q:

            for _ in range(len(q)):

                idx = q.popleft()

                if idx == n - 1:
                    return steps

                # Move Left
                if idx - 1 >= 0 and not visited[idx - 1]:

                    visited[idx - 1] = True
                    q.append(idx - 1)

                # Move Right
                if idx + 1 < n and not visited[idx + 1]:

                    visited[idx + 1] = True
                    q.append(idx + 1)

                # Prime Teleport
                val = nums[idx]

                if is_prime(val) and val not in used_prime:

                    for nxt in factor_map[val]:

                        if not visited[nxt]:

                            visited[nxt] = True
                            q.append(nxt)

                    used_prime.add(val)

            steps += 1

        return -1