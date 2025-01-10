from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Compute the maximum character frequencies for words2
        max_freq = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
        
        # Step 2: Filter words1 based on the max_freq
        universal_words = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_freq[char] for char in max_freq):
                universal_words.append(word)
        
        return universal_words