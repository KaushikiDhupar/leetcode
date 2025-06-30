class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # Ensure mid is even so it always points to the first element of a pair
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # Unique element is after this pair
                l = mid + 2
            else:
                # Unique element is before or at mid
                r = mid
        return nums[l]
