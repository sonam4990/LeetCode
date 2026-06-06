class Solution:
    def leftRightDifference(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            total_sum -= num  # right sum
            answer.append(abs(left_sum - total_sum))
            left_sum += num

        return answer