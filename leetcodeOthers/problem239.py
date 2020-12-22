from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        output = []

        for i, e in enumerate(nums):
            while queue:
                largest_element_index = queue[0]  # loop invariant

                if nums[largest_element_index] <= e:
                    queue.clear()  # removing all the elements from queue
                elif largest_element_index + (k - 1) < i:
                    # sliding makes largest element move out of the window
                    queue.popleft()
                elif nums[queue[-1]] <= e:
                    # last element of queue is less than the current element
                    queue.pop()
                else:
                    break

            queue.append(i)

            if i >= k - 1:
                output.append(nums[queue[0]])

        return output


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([5, 4, 3, 2, 1], 3))
    print(Solution().maxSlidingWindow([1, -1], 1))
    print(Solution().maxSlidingWindow([1], 1))
