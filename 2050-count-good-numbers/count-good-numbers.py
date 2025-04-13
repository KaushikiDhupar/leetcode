class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modu = 10**9 + 7
        
        def power(a, b):
            result = 1
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % modu
                a = (a * a) % modu
                b //= 2
            return result
        
        return (power(5, (n + 1) // 2) * power(4, n // 2)) % modu