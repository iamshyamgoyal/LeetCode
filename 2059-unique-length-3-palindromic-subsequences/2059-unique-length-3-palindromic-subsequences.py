class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_set = set()
        right_count = [0] * 26  
        
        for char in s:
            right_count[ord(char) - ord('a')] += 1
        
        unique_palindromes = set()
        
        for i, char in enumerate(s):
            middle = ord(char) - ord('a') 
            
            right_count[middle] -= 1
            
            for c in range(26):  
                if chr(c + ord('a')) in left_set and right_count[c] > 0:
                    palindrome = chr(c + ord('a')) + char + chr(c + ord('a'))
                    unique_palindromes.add(palindrome)
            
            left_set.add(char)
        
        return len(unique_palindromes)
