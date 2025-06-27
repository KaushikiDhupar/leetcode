class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #we are going to use the formula of total length-maximum frequency=total no of changes possible 
        maxlen,total,freq=0,0,0
        l=r=0
        n=len(s)
        #make a hashmap to store and find maximum frequency
        d={}
        while r<n:
            # Update frequency map
            d[s[r]] = d.get(s[r], 0) + 1
            max_freq=max(d.values())
            while ((r-l+1)-max_freq)>k:#condition not satisfied 
                #shrink window that is move l pointer
                d[s[l]]-=1
                l+=1
                
            else:#condition satisfied

                maxlen=max(maxlen,r-l+1)

            r+=1

        return maxlen
        