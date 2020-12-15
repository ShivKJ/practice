class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        A = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 1 + A[i - 1][j - 1]
                else:
                    A[i][j] = max(A[i - 1][j], A[i][j - 1])

        return A[-1][-1]
