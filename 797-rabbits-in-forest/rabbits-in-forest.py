class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        m, res = {}, 0
        for i in range(len(answers)):
            if m.__contains__(answers[i]):
                m[answers[i]] += 1
            else:
                m[answers[i]] = 1
        for i, j in m.items():
            while j>0:
                res += (i+1)
                j = j-i-1
        return res