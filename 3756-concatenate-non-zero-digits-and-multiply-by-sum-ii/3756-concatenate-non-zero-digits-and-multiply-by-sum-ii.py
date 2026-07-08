from typing import List

MOD = 10**9 + 7

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        # powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        size = 4 * n
        val = [0] * size
        sm = [0] * size
        cnt = [0] * size

        def build(idx, l, r):
            if l == r:
                d = ord(s[l]) - ord('0')
                if d != 0:
                    val[idx] = d
                    sm[idx] = d
                    cnt[idx] = 1
                return

            mid = (l + r) // 2
            build(idx * 2, l, mid)
            build(idx * 2 + 1, mid + 1, r)

            left = idx * 2
            right = idx * 2 + 1

            cnt[idx] = cnt[left] + cnt[right]
            sm[idx] = sm[left] + sm[right]
            val[idx] = (val[left] * pow10[cnt[right]] + val[right]) % MOD

        def query(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                return val[idx], sm[idx], cnt[idx]

            if r < ql or l > qr:
                return 0, 0, 0

            mid = (l + r) // 2

            lv, ls, lc = query(idx * 2, l, mid, ql, qr)
            rv, rs, rc = query(idx * 2 + 1, mid + 1, r, ql, qr)

            total_val = (lv * pow10[rc] + rv) % MOD
            total_sum = ls + rs
            total_cnt = lc + rc

            return total_val, total_sum, total_cnt

        build(1, 0, n - 1)

        ans = []

        for l, r in queries:
            v, ssum, _ = query(1, 0, n - 1, l, r)
            ans.append((v * ssum) % MOD)

        return ans