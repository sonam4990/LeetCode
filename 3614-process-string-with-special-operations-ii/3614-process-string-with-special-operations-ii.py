class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * (n + 1)

        for i, ch in enumerate(s):
            curr = lengths[i]

            if 'a' <= ch <= 'z':
                lengths[i + 1] = curr + 1
            elif ch == '*':
                lengths[i + 1] = max(0, curr - 1)
            elif ch == '#':
                lengths[i + 1] = curr * 2
            else:  # %
                lengths[i + 1] = curr

        if k >= lengths[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            before = lengths[i]

            if 'a' <= ch <= 'z':
                if k == before:
                    return ch

            elif ch == '#':
                if k >= before:
                    k -= before

            elif ch == '%':
                k = before - 1 - k

        return '.'