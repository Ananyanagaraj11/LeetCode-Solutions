class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Flatten the grid
        nums = sorted(val for row in grid for val in row)

        # Check if all numbers have the same remainder mod x
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1

        # Target = median (minimizes total operations)
        median = nums[len(nums) // 2]

        # Count operations
        ops = 0
        for num in nums:
            ops += abs(num - median) // x

        return ops
