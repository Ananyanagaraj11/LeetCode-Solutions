# 2833. Furthest Point From Origin
# Difficulty: Easy
# Topic: String, Counting

class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        L = moves.count('L')
        R = moves.count('R')
        wildcards = moves.count('_')
        return abs(L - R) + wildcards
