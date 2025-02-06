from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        count = 0
        for val in product_count.values():
            if val > 1:
                count += (val * (val - 1)) * 4
        
        return count