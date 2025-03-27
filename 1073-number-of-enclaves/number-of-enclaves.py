from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Apply BFS only on boundary land cells
        #in this question we are going to apply bfs only on boundary condition
        #after that anywhere there is a one connected to a boundary 1 we will mark it as -1
        #after that all the uneeded ones are eliminated then we can count the no of ones easily
        m, n = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = -1  # Mark as visited

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
                
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = -1
                        q.append((new_row, new_col))

        # Mark all boundary-connected land cells
        for i in range(m):
            if grid[i][0] == 1:
                bfs(i, 0)
            if grid[i][-1] == 1:
                bfs(i, n - 1)
        
        for j in range(n):
            if grid[0][j] == 1:
                bfs(0, j)
            if grid[m-1][j] == 1:
                bfs(m-1, j)

        # Count remaining land cells
        count = sum(grid[r][c] == 1 for r in range(m) for c in range(n))

        return count
