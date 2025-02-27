from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes=0
        q=deque()
        visited=set()
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
        directions=[(1,0),(0,1),(0,-1),(-1,0)]

        while q:
            row,col,minutes=q.popleft()
          

            for dr,dc in directions:
                new_row=dr+row
                new_col=dc+col
                if 0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]==1 and (new_row,new_col) not in visited:
                    grid[new_row][new_col]=2
                    q.append((new_row,new_col,minutes+1))
                    visited.add((new_row,new_col))
               
        return -1 if any(1 in row for row in grid) else minutes 


        
        