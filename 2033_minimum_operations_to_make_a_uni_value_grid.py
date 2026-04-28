# 2033. Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# Topic: Array, Math, Sorting, Matrix

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        nums = sorted(val for row in grid for val in row)

        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        median = nums[len(nums) // 2]

        ops = 0
        for num in nums:
            ops += abs(num - median) // x

        return ops
