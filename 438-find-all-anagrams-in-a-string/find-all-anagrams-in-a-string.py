class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        
        m = len(p)
        n = len(s)
        
        freq_pat = [0] * 26
        freq_wind = [0] * 26

        # Count frequency of characters in pattern
        for ch in p:
            freq_pat[ord(ch) - ord('a')] += 1

        # Initialize frequency of first window in text
        for i in range(m):
            freq_wind[ord(s[i]) - ord('a')] += 1

        res=[]
        if freq_wind == freq_pat:
            res.append(0)

        # Slide the window
        for i in range(m, n):
            freq_wind[ord(s[i]) - ord('a')] += 1                       # Add new character
            freq_wind[ord(s[i - m]) - ord('a')] -= 1                   # Remove old character

            if freq_wind == freq_pat:
                res.append(i-m+1)

        return res

        