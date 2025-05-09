class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        rows,cols=set(),set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for k in range(m):
            for l in range(n):
                if k in rows or l in cols:
                    matrix[k][l]=0
        return matrix

        return matrix

        
        """
        Do not return anything, modify matrix in-place instead.
        """
        