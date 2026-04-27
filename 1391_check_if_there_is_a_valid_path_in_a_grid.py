# 1391. Check if There is a Valid Path in a Grid
# Difficulty: Medium
# Topic: Union Find, BFS, DFS, Matrix

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        openings = {
            1: {2, 3},
            2: {0, 1},
            3: {2, 1},
            4: {3, 1},
            5: {2, 0},
            6: {3, 0},
        }

        delta = {
            0: (-1, 0),
            1: (1, 0),
            2: (0, -1),
            3: (0, 1),
        }

        opposite = {0: 1, 1: 0, 2: 3, 3: 2}

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

        for i in range(m):
            for j in range(n):
                for d in openings[grid[i][j]]:
                    dr, dc = delta[d]
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < m and 0 <= nj < n:
                        if opposite[d] in openings[grid[ni][nj]]:
                            union(i * n + j, ni * n + nj)

        return find(0) == find(m * n - 1)
