class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        left = moves.count('L')
        right = moves.count('R')
        blank = moves.count('_')
        
        return abs(right - left) + blank