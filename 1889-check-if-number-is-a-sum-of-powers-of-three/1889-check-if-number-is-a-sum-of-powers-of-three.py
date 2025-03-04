class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:  # If there's a '2' in base 3, it's not possible
                return False
            n //= 3  # Reduce n by a factor of 3
        return True
