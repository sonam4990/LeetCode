class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1

            elif nums[mid] < nums[right]:
                # Minimum is at mid or left half
                right = mid

            else:
                # Duplicate case
                right -= 1

        return nums[left]