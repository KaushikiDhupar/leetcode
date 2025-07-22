class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        def getComb(idx, curr):
            if idx == n:
                s = ''.join(curr)
                return [s]
            
            ch = int(digits[idx])
            l = []
            if ch < 7:
                for i in range(3):
                    o = chr(97 + (ch * 3 - 6) + i)
                    curr.append(o)
                    s = getComb(idx + 1, curr)
                    for j in s:
                        l.append(j)
                    curr.pop()

            elif ch == 7:
                for i in range(112, 116):
                    o = chr(i)
                    curr.append(o)
                    s = getComb(idx + 1, curr)
                    for j in s:
                        l.append(j)
                    curr.pop()
            elif ch == 8:
                for i in range(116, 119):
                    o = chr(i)
                    curr.append(o)
                    s = getComb(idx + 1, curr)
                    for j in s:
                        l.append(j)
                    curr.pop()
            else:
                for i in range(119, 123):
                    o = chr(i)
                    curr.append(o)
                    s = getComb(idx + 1, curr)
                    for j in s:
                        l.append(j)
                    curr.pop()

            return l
        
        if digits == '': return []
        return getComb(0, [])