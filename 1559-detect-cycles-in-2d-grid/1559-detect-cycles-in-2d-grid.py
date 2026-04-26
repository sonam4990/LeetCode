class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        # DFS function
        def dfs(r, c, pr, pc, char):

            # already visited -> cycle found
            if visited[r][c]:
                return True

            visited[r][c] = True

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # boundary check
                if 0 <= nr < rows and 0 <= nc < cols:

                    # same character
                    if grid[nr][nc] == char:

                        # don't go back to parent cell
                        if nr == pr and nc == pc:
                            continue

                        if dfs(nr, nc, r, c, char):
                            return True

            return False

        for r in range(rows):
            for c in range(cols):

                if not visited[r][c]:

                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True

        return False