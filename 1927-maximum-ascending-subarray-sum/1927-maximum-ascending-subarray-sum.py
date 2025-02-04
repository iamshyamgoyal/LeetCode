class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = []
        stack = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                stack.append(nums[i])
            else:
                result.append(sum(stack))
                stack = [nums[i]]
        
        result.append(sum(stack))
        
        return max(result)
