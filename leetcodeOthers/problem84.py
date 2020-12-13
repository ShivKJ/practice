from collections import deque
from typing import List


def largest_area_rectangle(heights: List[int]) -> int:
    """
    :param heights:
    :return:
    """
    stack = deque()
    curr_index = 0

    def width():
        """
        :return: rectangle width
        """
        return stack[-1] + 1 if stack else 0

    area = 0
    bars = len(heights)

    while curr_index < bars:
        if not stack or heights[stack[-1]] <= heights[curr_index]:
            stack.append(curr_index)
            curr_index += 1
        else:
            index = stack.pop()
            area = max(area, heights[index] * (curr_index - width()))

    while stack:
        index = stack.pop()
        area = max(area, heights[index] * (bars - width()))

    return area


if __name__ == '__main__':
    print(largest_area_rectangle([2, 1, 5, 6, 2, 3]))
    print(largest_area_rectangle([2, 1, 2]))
