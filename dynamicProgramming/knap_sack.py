from collections import namedtuple
from functools import lru_cache
from typing import List

Item = namedtuple('Item', 'w,v')


def max_profit(items: List[Item], max_weight):
    """
    Note: weight and value of each item must be integer. It weight is very
          large then it can result in memory issue
    :param items:
    :param max_weight:
    :return:
    """

    @lru_cache
    def profit(item_index, weight):
        """
        case-1:
                weight = 0 => profit = 0
        case-2:
                item_weight > weight => profit(item_index -1, weight) # item can not be selected
        case-3:
                max(
                        profit(item_index -1, weight), # item is not selected
                        item_value + profit(item_index -1, weight - item_weight) # item is not selected
                )
        :param item_index:
        :param weight:
        :return: total profit (value) of selected items
        """
        if weight <= 0 or item_index < 0:  # case-1
            return 0

        item = items[item_index]

        if item.w > weight:  # case-2
            return profit(item_index - 1, weight)

        # case-3
        return max(
            profit(item_index - 1, weight),
            item.v + profit(item_index - 1, weight - item.w)
        )

    optimal_profit = 0
    for i in range(len(items)):
        for j in range(1, max_weight + 1):
            optimal_profit = max(optimal_profit, profit(i, j))

    return optimal_profit  # equivalently, profit(len(items)-1, max_weight)
