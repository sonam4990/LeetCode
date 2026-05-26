class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        res = [0] * 26

        seen_lower = set()
        seen_upper = set()

        for c in word:

            # lowercase
            if ord(c) >= 97 and c not in seen_lower:
                res[ord(c) - 97] += 1
                seen_lower.add(c)

            # uppercase
            elif ord(c) <= 90 and c not in seen_upper:
                res[ord(c) - 65] += 1
                seen_upper.add(c)

        ans = 0

        for num in res:
            if num == 2:
                ans += 1

        return ans