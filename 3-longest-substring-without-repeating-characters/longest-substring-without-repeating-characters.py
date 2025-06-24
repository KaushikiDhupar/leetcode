class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen=0
        setx=set()

        for r in range(len(s)):
            if s[r] in setx:
                while l<r and s[r] in setx:
                    setx.remove(s[l])
                    l+=1
            setx.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen