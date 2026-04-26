# 3464. Maximize the Distance Between Points on a Square
# Difficulty: Hard
# Topic: Binary Search, Greedy, Sorting

import bisect

class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        perimeter = 4 * side

        def to_perimeter(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y

        pos = sorted(to_perimeter(x, y) for x, y in points)
        n = len(pos)
        pos2 = pos + [p + perimeter for p in pos]

        def can_achieve(d):
            for i in range(n):
                cur = i
                count = 1
                for _ in range(k - 1):
                    target = pos2[cur] + d
                    nxt = bisect.bisect_left(pos2, target, cur + 1)
                    if nxt >= 2 * n or pos2[nxt] > pos[i] + perimeter - d:
                        break
                    cur = nxt
                    count += 1
                if count == k:
                    return True
            return False

        lo, hi = 0, perimeter // k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_achieve(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
