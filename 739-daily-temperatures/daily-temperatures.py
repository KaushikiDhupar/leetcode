from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []  # stores indices of temperatures
        ans = [0] * len(temp)  # initialize answer list with 0s

        for i in range(len(temp)):
            # while stack not empty and current temp is greater than temp at index on top of stack
            while stack and temp[i] > temp[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans
