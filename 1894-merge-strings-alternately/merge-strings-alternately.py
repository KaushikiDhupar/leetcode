class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        i,j=0,0
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i,j=i+1,j+1
        res.append(word1[i:])
        res.append(word2[j:])
        
        return "".join(res)
        