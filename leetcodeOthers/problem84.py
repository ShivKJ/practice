from collections import deque
from typing import List


def largest_area_rectangle(heights: List[int]) -> int:
    """
    :param heights:
    :return:
    """
    stack = deque()
    curr_index = 0

    def prev_index():
        """
        :return: rectangle width
        """
        return stack[-1] + 1 if stack else 0

    def get_area():
        """
        :return: if item from stack is popped then calculating area
        """
        return heights[stack.pop()] * (curr_index - prev_index())

    area = 0
    
    while curr_index < len(heights):
        if not stack or heights[stack[-1]] <= heights[curr_index]:
            stack.append(curr_index)
            curr_index += 1
        else:
            area = max(area, get_area())

    while stack:
        area = max(area, get_area())

    return area


if __name__ == '__main__':
    print(largest_area_rectangle([2, 1, 5, 6, 2, 3]))
    print(largest_area_rectangle([2, 1, 2]))
