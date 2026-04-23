class Solution(object):
    def distance(self, nums):
        from collections import defaultdict

        # Group indices by their value
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        # For each group, compute distances using prefix sums
        arr = [0] * len(nums)

        for indices in groups.values():
            n = len(indices)
            if n == 1:
                continue

            # prefix_sum tracks sum of all positions
            prefix_sum = 0
            total_sum = sum(indices)

            for k, idx in enumerate(indices):
                left_count = k
                right_count = n - 1 - k

                left_dist = left_count * idx - prefix_sum
                right_dist = (total_sum - prefix_sum - idx) - right_count * idx

                arr[idx] = left_dist + right_dist
                prefix_sum += idx

        return arr
