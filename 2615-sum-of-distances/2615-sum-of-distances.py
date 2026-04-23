class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        pos = defaultdict(list)
        
        # Store indices for each number
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = [0] * len(nums)
        
        # Process each group of indices
        for indices in pos.values():
            
            n = len(indices)
            
            # Prefix sum of indices
            prefix = [0] * (n + 1)
            
            for i in range(n):
                prefix[i + 1] = prefix[i] + indices[i]
            
            total = prefix[n]
            
            for i, idx in enumerate(indices):
                
                # Distance from left side
                left = idx * i - prefix[i]
                
                # Distance from right side
                right = (total - prefix[i + 1]) - idx * (n - i - 1)
                
                ans[idx] = left + right
        
        return ans