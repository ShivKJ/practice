import numpy as np

from initialialSolution.vogel import Vogel


def run():
    # supply = np.array([1, 5, 3, 6, 8, 2, 6, 7, 9, 1, 0, 1])
    # demand = np.array([4, 2, 6, 1, 2, 9, 1, 10, 2, 3, 5, 4])
    # cost_martix = np.random.randint(0, 10, (demand.size, supply.size))
    # Vogel(cost_martix, supply, demand).solve()
    # supply = np.array([1, 5, 3, 2])
    # demand = np.array([2, 2, 6, 1])
    # cost_martix = np.random.randint(0, 10, (demand.size, supply.size))
    # Vogel(cost_martix, supply, demand).solve()

    supply = np.random.randint(1, 50, 3)
    demand = np.array(supply)
    np.random.shuffle(demand)

    cost_martix = np.random.randint(1, 20, (demand.size, supply.size))
    Vogel(cost_martix, supply, demand).solve()


if __name__ == '__main__':
    run()
