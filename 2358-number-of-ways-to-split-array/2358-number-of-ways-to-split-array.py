class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        prefix_sum = 0
        valid_splits = 0
        
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]  
            right_sum = total_sum - prefix_sum  
            
            if prefix_sum >= right_sum:
                valid_splits += 1
        
        return valid_splits
