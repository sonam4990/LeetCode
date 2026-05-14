class Solution:
    def isGood(self, nums):
        n = max(nums)

        # Length should be n + 1
        if len(nums) != n + 1:
            return False

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Numbers 1 to n-1 should appear once
        for i in range(1, n):
            if freq.get(i, 0) != 1:
                return False

        # Number n should appear twice
        if freq.get(n, 0) != 2:
            return False

        return True