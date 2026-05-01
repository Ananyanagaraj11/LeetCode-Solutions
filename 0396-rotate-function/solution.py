class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        # Compute F(0)
        f = 0
        for i in range(n):
            f += i * nums[i]

        best = f

        # Compute F(1), F(2), ... using the formula
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            if f > best:
                best = f

        return best
