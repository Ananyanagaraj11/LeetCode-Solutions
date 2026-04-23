# 1925. Count Square Sum Triples
# Difficulty: Easy
# Topic: Math, Brute Force

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                if c <= n and c * c == c_squared:
                    count += 1
        return count
