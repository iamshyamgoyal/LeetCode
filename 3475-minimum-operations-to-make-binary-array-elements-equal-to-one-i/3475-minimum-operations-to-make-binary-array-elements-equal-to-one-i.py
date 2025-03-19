from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0 if all(num == 1 for num in nums) else -1
        
        queue = deque()
        flips_affecting = 0
        total_flips = 0
        
        for i in range(n):
            # Remove flips that are no longer affecting the current i
            while queue and queue[0] < i - 2:
                queue.popleft()
                flips_affecting -= 1
            
            current_val = nums[i] ^ (flips_affecting % 2)
            
            if current_val == 0:
                if i > n - 3:
                    return -1
                queue.append(i)
                flips_affecting += 1
                total_flips += 1
        
        return total_flips