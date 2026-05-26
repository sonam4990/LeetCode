class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        s = set(word)
        count = 0
        
        for ch in s:
            
            if ch.islower() and ch.upper() in s:
                count += 1
        
        return count