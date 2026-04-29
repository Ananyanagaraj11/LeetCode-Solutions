# 3225. Maximum Score From Grid Operations
# Difficulty: Hard
# Topic: Array, DP, Matrix, Prefix Sum

class Solution(object):
    def maximumScore(self, grid):
        n = len(grid)
        N = n + 1

        pre = [[0] * N for _ in range(n)]
        for j in range(n):
            pj = pre[j]
            for i in range(n):
                pj[i + 1] = pj[i] + grid[i][j]

        NEG = -(1 << 62)
        size = N * N

        dp = [NEG] * size
        for b in range(N):
            dp[b] = 0

        for j in range(1, n):
            new_dp = [NEG] * size
            pre_j = pre[j]
            pre_jm1 = pre[j - 1]

            for b in range(N):
                m1 = NEG
                for a in range(b + 1):
                    v = dp[a * N + b]
                    if v > m1:
                        m1 = v

                suf = [NEG] * (N + 1)
                for a in range(n, b, -1):
                    v = dp[a * N + b]
                    s = suf[a + 1]
                    suf[a] = v if v > s else s

                pfx = [NEG] * N
                prev_pfx = NEG
                for a in range(b + 1, N):
                    v = dp[a * N + b]
                    if v != NEG:
                        v2 = v - pre_jm1[a]
                        if v2 > prev_pfx:
                            prev_pfx = v2
                    pfx[a] = prev_pfx

                pre_j_b = pre_j[b]
                bN = b * N

                for c in range(N):
                    left_c = pre_j_b - pre_j[c] if b > c else 0
                    best = NEG

                    if m1 != NEG:
                        nr = pre_jm1[c] - pre_jm1[b] if c > b else 0
                        v = m1 + nr
                        if v > best:
                            best = v

                    if c > b + 1:
                        pv = pfx[c - 1]
                        if pv != NEG:
                            v = pv + pre_jm1[c]
                            if v > best:
                                best = v

                    start = c if c > b else b + 1
                    if start <= n:
                        sv = suf[start]
                        if sv != NEG and sv > best:
                            best = sv

                    if best != NEG:
                        idx = bN + c
                        val = best + left_c
                        if val > new_dp[idx]:
                            new_dp[idx] = val

            dp = new_dp

        ans = 0
        for v in dp:
            if v > ans:
                ans = v
        return ans
