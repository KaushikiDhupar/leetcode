from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        visited=set()
        
        def bfs(r,c):
            q=deque()
            newarea=1
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()

                directions=[(0,1),(1,0),(0,-1),(-1,0)]
                for dr,dc in directions:
                    new_row=dr+row
                    new_col=dc+col
                    if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]==1 and (new_row,new_col) not in visited:
                        newarea+=1
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))
            return newarea
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and grid[i][j] not in visited:
                    new=bfs(i,j)
                    maxarea=max(new,maxarea)

        return maxarea
