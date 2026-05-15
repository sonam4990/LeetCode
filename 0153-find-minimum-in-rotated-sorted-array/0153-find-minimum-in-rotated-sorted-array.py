class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is at mid or left half
                right = mid

        return nums[left]