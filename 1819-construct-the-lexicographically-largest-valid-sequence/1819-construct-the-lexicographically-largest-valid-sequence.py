from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        result = [0] * size
        used = [False] * (n + 1)
        
        def backtrack(index: int) -> bool:
            if index == size:
                return True
            
            if result[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                
                if num == 1:
                    result[index] = 1
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[num] = False
                else:
                    if index + num >= size or result[index + num] != 0:
                        continue
                    
                    result[index] = result[index + num] = num
                    used[num] = True
                    
                    if backtrack(index + 1):
                        return True
                    
                    result[index] = result[index + num] = 0
                    used[num] = False
            
            return False
        
        backtrack(0)
        return result
