class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(s: str, target: int, index: int) -> bool:
            if index == len(s):
                return target == 0
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                if num > target:
                    break
                if can_partition(s, target - num, i + 1):
                    return True
            
            return False
        
        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i, 0):
                total += i * i
        
        return total
