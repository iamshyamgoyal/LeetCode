from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        
        # Count occurrences of each product
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        count = 0
        # Calculate number of valid tuples
        for val in product_count.values():
            if val > 1:
                count += (val * (val - 1)) * 4  # Each pair can be arranged in 4 ways
        
        return count