class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        counter=0
        i = 0
        while i < len(nums):  # use len(nums) because it changes after pop
            if nums[i] == val:
                nums.pop(i)
                counter += 1
                # don't increment i, because the list shifts left
            else:
                i += 1
        for j in range(counter):
            nums.append('_')
        return n-counter


        