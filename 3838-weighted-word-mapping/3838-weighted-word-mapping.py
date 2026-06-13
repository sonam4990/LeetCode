from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []

        for word in words:
            total_weight = 0

            for ch in word:
                total_weight += weights[ord(ch) - ord('a')]

            mod = total_weight % 26

            # 0 -> z, 1 -> y, ..., 25 -> a
            result.append(chr(ord('z') - mod))

        return "".join(result)