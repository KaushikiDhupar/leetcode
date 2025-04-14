class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 # returning true if n is greater than 0 and also anding n and n - 1 and if they are equal to 0, we return 0 
        