class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0   # double pointer
        r = n-1
        while l<r:
            while l<r and not s[l].isalnum():  # jump out of non-letter
                l += 1
            while l<r and not s[r].isalnum():  # jump out of non-letter
                r -= 1
            if s[l].lower() != s[r].lower():   # compare the valid char
                return False
            l += 1   
            r -= 1
        return True