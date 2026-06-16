class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for ch in s:
            if ch.islower():          # append letter
                result += ch

            elif ch == '*':          # remove last character
                if result:
                    result = result[:-1]

            elif ch == '#':          # duplicate string
                result += result

            elif ch == '%':          # reverse string
                result = result[::-1]

        return result