from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index, path, value, prev_operand):
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break

                curr_str = num[index:i+1]
                curr = int(curr_str)

                if index == 0:
                    backtrack(i + 1, curr_str, curr, curr)
                else:
                    backtrack(i + 1, path + '+' + curr_str, value + curr, curr)
                    backtrack(i + 1, path + '-' + curr_str, value - curr, -curr)
                    backtrack(i + 1, path + '*' + curr_str, value - prev_operand + prev_operand * curr, prev_operand * curr)

        backtrack(0, "", 0, 0)
        return res
