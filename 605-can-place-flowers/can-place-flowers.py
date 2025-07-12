class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left=i==0 or flowerbed[i-1]==0 #either we are standing at current on the first element or left side is safe
            right=i==len(flowerbed)-1 or flowerbed[i+1]==0 #either we are standing at current on the last element or right side is safe
            if left and right and flowerbed[i]==0:
                flowerbed[i]=1
                n-=1
            
        return n<=0

        