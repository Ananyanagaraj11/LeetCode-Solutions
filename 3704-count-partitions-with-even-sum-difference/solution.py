class Solution(object):
    def countPartitions(self, nums):
        total = sum(nums)
        if total % 2 == 0:
            return len(nums) - 1
        return 0
