class Solution:
    def maxValue(self, nums):
        
        n = len(nums)

        min_arr = [0] * n
        max_arr = [0] * n

        min_arr[-1] = nums[-1]
        max_arr[0] = nums[0]

        for i in range(1, n):
            max_arr[i] = max(nums[i], max_arr[i - 1])
            min_arr[n - i - 1] = min(nums[n - i - 1], min_arr[n - i])

        nums[n - 1] = max_arr[n - 1]

        for i in range(n - 2, -1, -1):

            if max_arr[i] > min_arr[i + 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i] = max_arr[i]

        return nums