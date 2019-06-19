from typing import List


class Item:
    """
    An item is defined by its weight and value.
    """

    def __init__(self, weight, value):
        self._weight = weight
        self._value = value

    @property
    def weight(self):
        return self._weight

    @property
    def value(self):
        return self._value

    @property
    def rate(self):
        return self.value / self.weight

    def __str__(self):
        return 'weight={};value={}'.format(self.weight, self.value)

    def __repr__(self):
        return str(self)


def non_zero(x, tol=1e-8):
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

    items = sorted(items, key=lambda x: x.rate, reverse=True)

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
