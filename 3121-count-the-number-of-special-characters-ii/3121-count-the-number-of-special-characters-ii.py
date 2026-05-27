class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        answer = 0

        # check all letters a-z
        for ch in "abcdefghijklmnopqrstuvwxyz":

            lower = ch
            upper = ch.upper()

            # both should exist
            if lower in word and upper in word:

                # last lowercase position
                last_lower = word.rfind(lower)

                # first uppercase position
                first_upper = word.find(upper)

                # lowercase before uppercase
                if last_lower < first_upper:
                    answer += 1

        return answer