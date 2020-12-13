from typing import List

from leetcodeOthers.problem84 import largest_area_rectangle


def maximal_rectangle(matrix: List[List[str]]):
    """
    finding largest rectangle area made of "1"s
    :param matrix:
    :return: max area
    """
    area = 0
    hist = None
    for row in matrix:
        row = [int(e) for e in row]

        if hist:
            hist = [hist[i] + 1 if row[i] == 1 else 0 for i in range(len(row))]
        else:
            hist = row

        area = max(area, largest_area_rectangle(hist))

    return area


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(maximal_rectangle(matrix))
