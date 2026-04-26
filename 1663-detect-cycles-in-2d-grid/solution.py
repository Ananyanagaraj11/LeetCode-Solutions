class Solution(object):
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])

        # Union-Find with path compression + union by rank
        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return True  # already connected = CYCLE!
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return False

        for i in range(m):
            for j in range(n):
                idx = i * n + j

                # Check RIGHT neighbor
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if union(idx, idx + 1):
                        return True

                # Check DOWN neighbor
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if union(idx, idx + n):
                        return True

        return False
