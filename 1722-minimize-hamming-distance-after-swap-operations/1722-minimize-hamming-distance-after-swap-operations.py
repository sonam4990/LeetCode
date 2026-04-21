from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        
        # DSU (Union Find)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Build components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Group indices by root
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)
        
        # Calculate minimum Hamming distance
        res = 0
        
        for indices in groups.values():
            count = Counter()
            
            # Count source values
            for i in indices:
                count[source[i]] += 1
            
            # Match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    res += 1
        
        return res