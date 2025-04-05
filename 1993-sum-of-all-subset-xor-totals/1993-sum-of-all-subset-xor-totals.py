class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, curr_xor):
            if index == len(nums):
                return curr_xor
            # Include nums[index] in the subset
            with_curr = dfs(index + 1, curr_xor ^ nums[index])
            # Exclude nums[index] from the subset
            without_curr = dfs(index + 1, curr_xor)
            return with_curr + without_curr
        
        return dfs(0, 0)
