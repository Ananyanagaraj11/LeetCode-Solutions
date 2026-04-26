# 1559. Detect Cycles in 2D Grid
# Difficulty: Medium
# Topic: Union Find, DFS, BFS, Matrix

class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return True
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return False

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if union(idx, idx + 1):
                        return True
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if union(idx, idx + n):
                        return True

        return False
