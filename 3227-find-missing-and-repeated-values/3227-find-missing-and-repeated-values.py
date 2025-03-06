from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_sum = (n * n * (n * n + 1)) // 2  # Sum of first n^2 natural numbers
        actual_sum = 0
        num_count = {}  # Dictionary to count occurrences
        
        repeated = -1
        missing = -1
        
        for row in grid:
            for num in row:
                actual_sum += num
                if num in num_count:
                    repeated = num  # Found the repeated number
                num_count[num] = num_count.get(num, 0) + 1
        
        missing = expected_sum - (actual_sum - repeated)  # Derive the missing number
        
        return [repeated, missing]
