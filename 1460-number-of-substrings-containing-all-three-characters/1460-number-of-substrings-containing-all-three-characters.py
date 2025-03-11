class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            while all(count[ch] > 0 for ch in 'abc'):
                # If the window [left, right] contains at least one 'a', 'b', and 'c'
                result += len(s) - right
                count[s[left]] -= 1
                left += 1
                
        return result
