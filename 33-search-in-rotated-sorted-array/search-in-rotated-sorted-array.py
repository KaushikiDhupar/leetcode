class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #since its a rotated sorted array first we search for pivot element that is the smallest element and assign to r
        def findpivot(nums):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1 #then minimum element lies on right side discarding the mid because it is already greater than r
                else:
                    r = mid #either the mid we found is the min element or min element is on the left side
            return r  # pivot index

        def binarySearch(nums, l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1   
                elif nums[mid] < target:
                    l = mid + 1    
                else:
                    return mid
            return -1

        pivot = findpivot(nums)

        # ✅ Handle pivot = 0 case safely
        if pivot > 0:
            ans_index = binarySearch(nums, 0, pivot - 1, target)
            if ans_index != -1:
                return ans_index

        return binarySearch(nums, pivot, len(nums) - 1, target)
