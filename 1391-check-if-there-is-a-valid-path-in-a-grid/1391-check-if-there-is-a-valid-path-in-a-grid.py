class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        # directions
        # left, right, up, down
        directions = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }

        visited = set()

        queue = deque([(0, 0)])

        while queue:

            r, c = queue.popleft()

            if (r, c) == (rows - 1, cols - 1):
                return True

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # current street type
            street = grid[r][c]

            for dr, dc in directions[street]:

                nr = r + dr
                nc = c + dc

                # boundary check
                if 0 <= nr < rows and 0 <= nc < cols:

                    next_street = grid[nr][nc]

                    # check if next cell connects back
                    if (-dr, -dc) in directions[next_street]:

                        queue.append((nr, nc))

        return False