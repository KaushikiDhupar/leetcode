class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        seen=set()
        l,r=0,0
        while r<n:
            if abs(r-l)>k:
                seen.remove(nums[l])
                l+=1
            #if we have seen in past  nums[r]
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
            r+=1
        return False

        