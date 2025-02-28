class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # Step 1: Compute LCS table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Step 2: Build SCS by backtracking the LCS table
        i, j = m, n
        result = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # Common character (part of LCS)
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:  # Pick from str1
                result.append(str1[i - 1])
                i -= 1
            else:  # Pick from str2
                result.append(str2[j - 1])
                j -= 1
        
        # Add remaining characters if any
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        # Reverse to get the final result
        return "".join(result[::-1])
