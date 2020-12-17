from typing import List


class Solution:
    def maxProfit(self, max_transaction: int, prices: List[int]) -> int:
        if not max_transaction or not prices:
            # nothing to do
            return 0

        n = len(prices)
        A = [[0] * n for _ in range(max_transaction)]  # max_transaction X n

        for k in range(max_transaction):
            max_diff = -prices[0]

            for i in range(n):
                """
                let A[k][i] = profit from max of k-transaction done up to i-th day
                We can find recursive formula in the following way
                1) either we do not choose to do transaction (no purchase or sell) on ith day
                2) we do sell on ith day
                
                A[k][i] = max(
                                A[k][i-1] if i > 0 else 0,
                                max(prices[i] - prices[m] + (A[k-1][m] if k > 0 else 0) for m in range(j))
                        )
                 
                """
                A[k][i] = max(A[k][i - 1], max_diff + prices[i])
                max_diff = max(max_diff, A[k - 1][i] - prices[i])

        return A[-1][-1]


if __name__ == '__main__':
    arr = [2, 5, 7, 1, 4, 3, 1, 3]
    print(Solution().maxProfit(3, arr))
