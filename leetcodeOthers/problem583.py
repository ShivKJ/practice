class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        A = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    if i == 0 or j == 0:
                        A[i][j] = i + j
                    else:
                        A[i][j] = A[i - 1][j - 1]
                else:
                    if i == 0 and j != 0:
                        A[i][j] = A[i][j - 1] + 1
                    elif i != 0 and j == 0:
                        A[i][j] = A[i - 1][j] + 1
                    else:
                        A[i][j] = 1 + min(A[i - 1][j], A[i][j - 1])

        return A[-1][-1]
