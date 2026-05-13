class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        
        # Difference array
        diff = [0] * (2 * limit + 2)

        left = 0
        right = n - 1

        while left < right:
            a = nums[left]
            b = nums[right]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # Default: 2 moves
            diff[2] += 2

            # 1 move range
            diff[low] -= 1
            diff[high + 1] += 1

            # 0 move at exact sum
            diff[s] -= 1
            diff[s + 1] += 1

            left += 1
            right -= 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans