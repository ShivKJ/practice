from typing import List


class Solution:
    def maxProfit(self, max_transaction: int, prices: List[int]) -> int:
        if not max_transaction or not prices:
            # nothing to do
            return 0

        total_days = len(prices)
        A = [[0] * total_days for _ in range(1 + max_transaction)]  # max_transaction X n

        for transaction in range(1, max_transaction + 1):
            max_diff = A[transaction - 1][0] - prices[0]

            for day in range(1, total_days):
                """
                let A[k][i] = profit from max of k-transaction done up to i-th day
                We can find recursive formula in the following way
                1) either we do not choose to do transaction (no purchase or sell) on ith day
                2) we do sell on ith day
                
                A[k][i] = max(
                                A[k][i-1],
                                prices[i] + (max(A[k-1][m] - prices[m])  
                                    for m in range(1, j)
                        )
                 
                 (max(A[k-1][m] - prices[m]) = total cost incurred if a purchased is made on mth day
                 prices[i] + (max(A[k-1][m] - prices[m]) = total profit if purchased on mth day and sold on ith day
                """
                A[transaction][day] = max(A[transaction][day - 1], max_diff + prices[day])
                max_diff = max(max_diff, A[transaction - 1][day] - prices[day])

        return A[-1][-1]
