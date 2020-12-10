def longest_increasing_subsequence_mathematical_formulation(arr):
    """
    let X[i] be bool variable which is 1 if ith value from array "arr" is selected in LIS, else 0.

    objective function is simply maximise X[0] + X[1] + .... X[n-1], n = length of arr

    Two elements arr[i] and arr[j] can not be part of LIS if arr[j] is more than or equal
    to arr[i] and j < i, or equivalently
                X[i] + X[j] <= 1 if j < i and arr[j] >= arr[i]  (for non decreasing case use arr[j] > arr[i])

    :param arr:
    :return: LIS length
    """
    from ortools.linear_solver.pywraplp import Solver
    solver = Solver('LIS', Solver.SCIP_MIXED_INTEGER_PROGRAMMING)

    n = len(arr)
    X = [solver.BoolVar(f'{i}') for i in range(n)]

    objective = solver.Objective()
    objective.SetMaximization()

    for x in X:
        objective.SetCoefficient(x, 1)

    for i in range(n):
        for j in range(i):
            if arr[j] >= arr[i]:  # previously occurring element is not less than ith element so
                # either ith or jth element will be present in LIS
                constraint = solver.Constraint(0, 1, f'{i}_{j}')

                constraint.SetCoefficient(X[i], 1)
                constraint.SetCoefficient(X[j], 1)

    solver.Solve()

    return int(objective.Value())


def longest_increasing_subsequence_iterative(arr):
    """
    let LIS(i) be length of largest increasing subsequence up to index i, then

        LIS(i) = max(LIS(j), j < i and arr[j] < arr[i], default=1), i = 0, 1, 2,... n-1

    that is if ith element is chosen to be part of LIS then we check, which previous
    element can also be in LIS. If jth element is chosen, then LIS(i) = 1 + LIS(j).
    Of course, if no such j exists then default value is 1

    :param arr:
    :return: length of LIS
    """
    n = len(arr)
    output = [0] * n

    for i in range(n):
        output[i] = max(
            (
                output[j] + 1 for j in range(i) if arr[i] > arr[j]
            ),
            default=1
        )

    return output[-1]


if __name__ == '__main__':
    print(longest_increasing_subsequence_iterative([3, 4, -1, 0, 6, 2, 3]))
    print(longest_increasing_subsequence_mathematical_formulation([3, 4, -1, 0, 6, 2, 3]))
    print(longest_increasing_subsequence_mathematical_formulation([7, 7, 7, 7, 7]))
