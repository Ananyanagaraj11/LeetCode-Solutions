# 3432. Count Partitions with Even Sum Difference
# Difficulty: Easy
# Topic: Array, Math

class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        if total % 2 == 0:
            return len(nums) - 1
        return 0
