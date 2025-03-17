class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                del dict[i]
            else:
                dict[i] = 1
        
        if dict:
            return False
        return True