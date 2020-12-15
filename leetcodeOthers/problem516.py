class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        A = [[0] * n for _ in range(n)]

        for i in range(n):
            A[i][i] = 1

        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    A[i][j] = 2 + A[i + 1][j - 1]
                else:
                    A[i][j] = max(A[i + 1][j], A[i][j - 1])

        return A[0][-1]
