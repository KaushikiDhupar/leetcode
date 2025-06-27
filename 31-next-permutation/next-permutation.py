from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums) - 1
        marked_index = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n, 0, -1):
            if nums[i - 1] < nums[i]:
                marked_index = i - 1
                break

        print("Marked index:", marked_index)

        # Step 2: If no such index, reverse the whole array
        if marked_index == -1:
            nums.reverse()
            print("Reversed entire array:", nums)
            return

        # Step 3: Find element to swap
        swap_index = marked_index
        for i in range(n, marked_index, -1):
            if nums[marked_index] < nums[i]:
                swap_index = i
                break

        print("Swap index:", swap_index)

        # Swap
        nums[marked_index], nums[swap_index] = nums[swap_index], nums[marked_index]
        print("After swap:", nums)

        # Reverse suffix
        nums[marked_index + 1:] = nums[marked_index + 1:][::-1]
        print("Final result:", nums)
