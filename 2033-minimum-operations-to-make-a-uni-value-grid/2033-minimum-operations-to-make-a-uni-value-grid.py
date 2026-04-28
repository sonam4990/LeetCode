class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        # flatten grid
        nums = []

        for row in grid:
            nums.extend(row)

        # check if possible
        remainder = nums[0] % x

        for num in nums:
            if num % x != remainder:
                return -1

        # sort numbers
        nums.sort()

        # median minimizes operations
        target = nums[len(nums) // 2]

        operations = 0

        for num in nums:
            operations += abs(num - target) // x

        return operations 