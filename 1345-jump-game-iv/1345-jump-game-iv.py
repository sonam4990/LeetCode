from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):

        n = len(arr)

        if n == 1:
            return 0

        # Store indices having same value
        graph = defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([(0, 0)])   # (index, steps)
        visited = set([0])

        while queue:

            index, steps = queue.popleft()

            # Reached last index
            if index == n - 1:
                return steps

            neighbors = []

            # i - 1
            if index - 1 >= 0:
                neighbors.append(index - 1)

            # i + 1
            if index + 1 < n:
                neighbors.append(index + 1)

            # Same value jumps
            neighbors.extend(graph[arr[index]])

            for nxt in neighbors:

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            # Important optimization
            graph[arr[index]].clear()  