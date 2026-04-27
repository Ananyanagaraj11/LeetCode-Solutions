class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # Each street type opens to which directions
        # Directions: 0=up, 1=down, 2=left, 3=right
        openings = {
            1: {2, 3},      # left, right
            2: {0, 1},      # up, down
            3: {2, 1},      # left, down
            4: {3, 1},      # right, down
            5: {2, 0},      # left, up
            6: {3, 0},      # right, up
        }

        # direction -> (row_change, col_change)
        delta = {
            0: (-1, 0),   # up
            1: (1, 0),    # down
            2: (0, -1),   # left
            3: (0, 1),    # right
        }

        # opposite directions (must match for connection)
        opposite = {0: 1, 1: 0, 2: 3, 3: 2}

        # Union-Find
        parent = list(range(m * n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        # Connect cells
        for i in range(m):
            for j in range(n):
                for d in openings[grid[i][j]]:
                    dr, dc = delta[d]
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < m and 0 <= nj < n:
                        # Does neighbor accept from opposite direction?
                        if opposite[d] in openings[grid[ni][nj]]:
                            union(i * n + j, ni * n + nj)

        return find(0) == find(m * n - 1)
