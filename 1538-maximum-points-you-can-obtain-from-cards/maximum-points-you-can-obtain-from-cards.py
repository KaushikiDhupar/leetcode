class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum,rsum,maxsum=0,0,0
        for i in range(k):
            lsum=lsum+cardPoints[i]
        maxsum=lsum
        right=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum=lsum-cardPoints[i]
            rsum=rsum+cardPoints[right]
            right=right-1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum
        