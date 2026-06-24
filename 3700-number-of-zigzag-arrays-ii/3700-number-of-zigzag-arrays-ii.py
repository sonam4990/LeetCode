class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        if n == 1:
            return m

        size = 2 * m

        def mat_mul(A, B):
            C = [[0] * size for _ in range(size)]

            for i in range(size):
                for k in range(size):
                    if A[i][k]:
                        a = A[i][k]

                        for j in range(size):
                            if B[k][j]:
                                C[i][j] = (
                                    C[i][j]
                                    + a * B[k][j]
                                ) % MOD

            return C

        def mat_pow(M, power):
            R = [[0] * size for _ in range(size)]

            for i in range(size):
                R[i][i] = 1

            while power:
                if power & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                power >>= 1

            return R

        trans = [[0] * size for _ in range(size)]

        for v in range(m):

            up = v
            down = m + v

            for w in range(v):
                trans[up][m + w] = 1

            for w in range(v + 1, m):
                trans[down][w] = 1

        init = [0] * size

        for a in range(m):
            for b in range(m):

                if a < b:
                    init[b] += 1

                elif a > b:
                    init[m + b] += 1

        P = mat_pow(trans, n - 2)

        final = [0] * size

        for i in range(size):
            if init[i]:

                for j in range(size):
                    final[j] = (
                        final[j]
                        + init[i] * P[i][j]
                    ) % MOD

        return sum(final) % MOD