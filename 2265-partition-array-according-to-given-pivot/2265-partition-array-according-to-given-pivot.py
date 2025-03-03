from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        equal_to = []
        greater_than = []
        
        # Partition elements into three lists
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num > pivot:
                greater_than.append(num)
            else:
                equal_to.append(num)
        
        # Concatenate the lists to get the final result
        return less_than + equal_to + greater_than