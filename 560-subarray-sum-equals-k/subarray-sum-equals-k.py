class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap={0:1}
        ans=0
        curr=0
        for num in nums:
            curr+=num
            residue=curr-k
            ans+=prefixMap.get(residue,0)
            prefixMap[curr]=1+prefixMap.get(curr,0)
        return ans
                    
            
        
        