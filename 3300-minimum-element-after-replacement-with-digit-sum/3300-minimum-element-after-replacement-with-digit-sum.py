class Solution:
    def minElement(self, nums):
        
        minimum = float('inf')

        for num in nums:

            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            minimum = min(minimum, digit_sum)

        return minimum