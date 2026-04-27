class Solution(object):
    def maxDistance(self, side, points, k):
        import bisect

        perimeter = 4 * side

        # Step 1: Map (x,y) to clockwise perimeter position
        def to_perimeter(x, y):
            if y == 0:          # bottom edge
                return x
            elif x == side:     # right edge
                return side + y
            elif y == side:     # top edge
                return 3 * side - x
            else:               # left edge (x == 0)
                return 4 * side - y

        pos = sorted(to_perimeter(x, y) for x, y in points)
        n = len(pos)

        # Double the array to handle circular wrap-around
        pos2 = pos + [p + perimeter for p in pos]

        # Step 2: Check if we can pick k points with min gap >= d
        def can_achieve(d):
            for i in range(n):              # try each starting point
                cur = i
                count = 1
                for _ in range(k - 1):      # pick k-1 more
                    target = pos2[cur] + d
                    nxt = bisect.bisect_left(pos2, target, cur + 1)
                    # Make sure last point leaves room to wrap back
                    if nxt >= 2 * n or pos2[nxt] > pos[i] + perimeter - d:
                        break
                    cur = nxt
                    count += 1
                if count == k:
                    return True
            return False

        # Step 3: Binary search on the answer
        lo, hi = 0, perimeter // k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_achieve(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
