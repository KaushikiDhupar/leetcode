class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag=False
        n=len(nums)
        seen=set()
        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            if len(seen)>k:
                seen.remove(nums[r-k])

            r+=1
        return False
