from dataclasses import dataclass
from operator import attrgetter
from typing import List


@dataclass
class Item:
    """
    An item is defined by its weight and value.
    """
    weight: float
    value: float

    @property
    def rate(self) -> float:
        """
        :return: value per unit weight
        """
        return self.value / self.weight


def non_zero(x, tol=1e-8) -> bool:
    """
    :param x:
    :param tol:
    :return: True if absolute value of x is less than tol
    """
    return abs(x) > tol


def get_items(items: List[Item], max_cap) -> List[Item]:
    """
    In fractional knapsack problem, from given items (an
    item is defined by its weight and value) select items in
    such a way so that total value of selected items is maximized.
    Note that an item can be split.

    To do so, firstly given list of items is sorted in descending
    order of value / weight which is rate of item per unit mass.
    Then items are selected until weight of selected item overcomes
    max_cap or there is no remaining item.

    If it is not possible to select a whole item then the item is
    split and added to the desired list of items.

    :param items:
    :param max_cap:
    :return: selected items.
    """

    items = sorted(items, key=attrgetter('rate'), reverse=True)

    output = []

    picked_wt = 0

    for item in items:
        wt_to_pick = min(item.weight, max_cap - picked_wt)

        if wt_to_pick == item.weight:
            output.append(item)

            picked_wt += wt_to_pick

        else:
            if non_zero(wt_to_pick):  # creating a fractional item.
                equivalent_value = wt_to_pick * item.rate

                output.append(Item(wt_to_pick, equivalent_value))

            break

    return output


if __name__ == '__main__':
    items = [Item(10, 40), Item(20, 90), Item(30, 120)]
    print(get_items(items, 40))
