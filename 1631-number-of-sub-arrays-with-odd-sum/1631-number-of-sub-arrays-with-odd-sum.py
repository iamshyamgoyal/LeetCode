from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # To account for subarrays starting from index 0
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                result = (result + even_count) % MOD
                odd_count += 1
        
        return result