from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for tile in counter:
                if counter[tile] > 0:
                    total += 1
                    counter[tile] -= 1
                    total += backtrack(counter)
                    counter[tile] += 1
            return total
        
        return backtrack(Counter(tiles))