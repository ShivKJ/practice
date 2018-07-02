from logging import getLogger, DEBUG

from numpy import ndarray, where, partition, array, zeros_like

from logger import LOGGER_NAME

logger = getLogger(LOGGER_NAME)
_MAX = 1 << 30

_TOLERANCE = 1e-8
_SUPPLY_AXIS, _DEMAND_AXIS = 0, 1


def _diff_of_2_min(cost_matrix: ndarray, axis: int) -> ndarray:
    '''
    Finds diff of two minimum; either row wise(DEMAND AXIS) operationR column wise(SUPPLY AXIS)
    :param cost_matrix:
    :param axis:
    :return:
    '''
    if axis is _DEMAND_AXIS:
        cost_matrix = cost_matrix.T

    a, b = partition(cost_matrix, 2, _SUPPLY_AXIS)[:2]

    return where(a == _MAX, b, where(b == _MAX, a, abs(a - b)))


def _max_arg(arr: ndarray) -> int:
    '''
    Finds max arg which don't corresponds to MAX value.
    If no such element is present then return 0
    :param arr:
    :return:
    '''

    prev = None
    idx = 0

    for i, elem in enumerate(arr):
        if elem != _MAX:
            if prev is None or prev < elem:
                prev = elem
                idx = i
    return idx


class Vogel:
    '''
        Implementation Note: Vogel method is used to find better initial solution from Northwest-
                            method.
                            It also considers CostMatrix while finding initial solution.
                            Steps:
                                1) For each row and column, absolute difference between two lowest
                                    element is found. Row operationR column having max difference is
                                    selected.
                                2) Suppose it is a row which has max difference, then at
                                    index of minimum element in row, min of amount of supply and
                                    demand is given. If supply is exhausted then column is crossed
                                    else row is crossed.
                                3)  This process is repeated until all rows and columns are
                                    crossed.

            (COST_MATRIX)(demand)(difference of two lowest element in row)
                 ^           ^    ^
                 |           |    |
            0	4	2	5	|2   #2
            9	5	3	7	|2   #2
            5	5  '0'	6	|6   #5  <- MAX_DIFF
            0	2	7	0	|1   #0
            --------------------------------
            1	5	3	2     <- (supply)
            #	#	#	#
            0	2	2	5     <- (difference of two lowest element in column)

            0	4	*	5	|2   #4
            9	5	*	7	|2   #2
            5	5	*	6	|3   #0
            0	2	*  '0'	|1   #0
            --------------------------------
            1	5	0	2
            #	#	#	#
            0	2	*	5
                        ^
                        |
                    MAX_DIFF

           '0'	4	*	5	|2   #4
            9	5	*	7	|2   #2
            5	5	*	6	|3   #0
            *	*	*	*	|0   #*
            --------------------------------
            1	5	0	1
            #	#	#	#
            5	1	*	1
            ^
            |
        MAX_DIFF

            *	4	*	5	|1   #1
            *  '5'	*	7	|2   #2  <- MAX_DIFF
            *	5	*	6	|3   #1
            *	*	*	*	|0   #*
            --------------------------------
            0	5	0	1
            #	#	#	#
            *	1	*	1

            *  '4'	*	5	|1   #1 <- MAX_DIFF
            *	*	*	*	|0   #*
            *	5	*	6	|3   #1
            *	*	*	*	|0   #*
            --------------------------------
            0	3	0	1
            #	#	#	#
            *	1	*	1

            *	*	*	*	|0   #*
            *	*	*	*	|0   #*
            *	5	*  '6'	|3   #1
            *	*	*	*	|0   #*
            --------------------------------
            0	2	0	1
            #	#	#	#
            *	5	*	6
                        ^
                        |
                    MAX_DIFF

            *	*	*	*	|0   #*
            *	*	*	*	|0   #*
            *	5	*	*	|2   #5 <- MAX_DIFF
            *	*	*	*	|0   #*
            --------------------------------
            0	2	0	0
            #	#	#	#
            *	5	*	*

            *	*	*	*	|0   #*
            *	*	*	*	|0   #*
            *	*	*	*	|0   #*
            *	*	*	*	|0   #*
            --------------------------------
            0	0	0	0
            #	#	#	#
            *	*	*	*
    '''

    def __init__(self, cost_matrix: ndarray, supply: ndarray, demand: ndarray):
        # problem should be balanced
        assert abs(supply.sum() - demand.sum()) <= _TOLERANCE

        self._cost_matrix = array(cost_matrix)
        self._supply = array(supply)
        self._demand = array(demand)

        self._supply_diff = None
        self._demand_diff = None
        self._output = zeros_like(cost_matrix)

    def _update_supply_diff(self):
        self._supply_diff = _diff_of_2_min(self._cost_matrix, _SUPPLY_AXIS)

    def _update_demand_diff(self):
        self._demand_diff = _diff_of_2_min(self._cost_matrix, _DEMAND_AXIS)

    def log_steps(self):
        '''
        Only logs if mode is debug.
        '''
        if not logger.isEnabledFor(DEBUG):
            return

        NAN = '*'

        rows = ['', '']

        def X(row):
            def append(x):
                row.append(NAN if x == _MAX else str(x))
                return append

            return append

        def join(row):
            rows.append(''.join(row))

        def append(row):
            tmp = []

            holder = X(tmp)
            for x in row:
                holder(x)('\t')

            join(tmp)

        for i in range(len(self._demand)):
            row = []
            holder = X(row)

            for j in range(len(self._supply)):
                holder(self._cost_matrix[i][j])('\t')

            holder('|')(self._demand[i])('   #')(self._demand_diff[i])

            join(row)

        rows.append(''.join(['--------'] * len(self._supply)))

        append(self._supply)
        append(['#'] * len(self._supply))
        append(self._supply_diff)

        rows.append('')

        logger.debug('\n'.join(rows))

    def solve(self) -> ndarray:

        self._update_demand_diff()
        self._update_supply_diff()

        supply = self._supply.sum()

        while abs(supply) > _TOLERANCE:
            self.log_steps()

            supply_idx = _max_arg(self._supply_diff)
            demand_idx = _max_arg(self._demand_diff)

            high_supply = (self._supply_diff[supply_idx] != _MAX and
                           self._supply_diff[supply_idx] > self._demand_diff[demand_idx])

            if high_supply:
                demand_idx = self._cost_matrix[:, supply_idx].argmin()
            else:
                supply_idx = self._cost_matrix[demand_idx].argmin()

            if self._supply[supply_idx] > self._demand[demand_idx]:
                transferred = self._demand[demand_idx]

                self._supply[supply_idx] -= transferred
                self._demand[demand_idx] = 0
                self._demand_diff[demand_idx] = _MAX
                self._cost_matrix[demand_idx, :] = _MAX
                self._update_supply_diff()
            else:
                transferred = self._supply[supply_idx]

                self._demand[demand_idx] -= transferred
                self._supply[supply_idx] = 0
                self._supply_diff[supply_idx] = _MAX
                self._cost_matrix[:, supply_idx] = _MAX
                self._update_demand_diff()

            supply -= transferred
            self._output[demand_idx][supply_idx] = transferred

        self.log_steps()

        return self._output
