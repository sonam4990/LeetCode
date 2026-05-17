class Solution:
    def canReach(self, arr, start):

        visited = set()

        def dfs(i):

            # Out of bounds
            if i < 0 or i >= len(arr):
                return False

            # Already visited
            if i in visited:
                return False

            # Reached value 0
            if arr[i] == 0:
                return True

            visited.add(i)

            # Jump forward or backward
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)