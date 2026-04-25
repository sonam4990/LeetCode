from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Step 1: Map 2D points to 1D positions along the perimeter
        # We also need to keep the original coordinates for Manhattan calculation
        perimeter_points = []
        for x, y in points:
            if y == 0:          # Bottom
                d = x
            elif x == side:     # Right
                d = side + y
            elif y == side:     # Top
                d = 2 * side + (side - x)
            else:               # Left
                d = 3 * side + (side - y)
            perimeter_points.append((d, x, y))
        
        # Sort by 1D position
        perimeter_points.sort()
        n = len(perimeter_points)

        def get_manhattan(p1, p2):
            return abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

        def check(mid_dist):
            # Try different starting points due to circular nature
            # Since k is small, we only need to try a few starting indices
            for start_idx in range(min(n, n // k + 1)):
                count = 1
                last_pt = perimeter_points[start_idx]
                
                for j in range(start_idx + 1, n):
                    # Validate against the current 'mid_dist'
                    if get_manhattan(last_pt, perimeter_points[j]) >= mid_dist:
                        # Additionally, check distance to the VERY FIRST point 
                        # to maintain the minimum distance across the wrap-around
                        if count == k - 1:
                            if get_manhattan(perimeter_points[j], perimeter_points[start_idx]) >= mid_dist:
                                return True
                        else:
                            count += 1
                            last_pt = perimeter_points[j]
            return False

        # Step 2: Binary Search on the possible answer
        low = 1
        high = 2 * side # Max Manhattan distance possible in a square
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans