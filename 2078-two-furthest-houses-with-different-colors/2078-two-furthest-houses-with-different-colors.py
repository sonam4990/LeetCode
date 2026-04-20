class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        
        max_dist = 0
        
        # Compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = i
                break
        
        # Compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break
        
        return max_dist