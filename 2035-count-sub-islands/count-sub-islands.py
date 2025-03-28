class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid2),len(grid2[0])
        visit=set()
        res=True

        def dfs(i,j):
            #base case
            if (i<0 or j<0 or i>=m or j>=n or grid2[i][j]==0 or (i,j) in visit):
                return True
            #code for current cell check so first we will add it to visit set 
            
            visit.add((i,j))
            res=True #set flag true
            #check its corresponding grid 1 cell if its 0 then res is returned false
            if grid1[i][j]==0:
                res=False
            res=dfs(i,j-1) and res #if cell has one in grid2,then res=True ,if dfs==true then dfs=1 and res=1 res=True
            res=dfs(i,j+1) and res
            res=dfs(i-1,j) and res
            res=dfs(i+1,j) and res
            return res
        count=0
        for r in range(m):
            for c in range(n):
                if grid2[r][c]==1 and(r,c) not in visit and dfs(r,c):
                    count+=1
        return count

