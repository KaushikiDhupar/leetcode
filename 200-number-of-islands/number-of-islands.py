from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # Base condition: Out of bounds or already visited (water)
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != '1':
                return
            
            grid[i][j] = '0'  # Mark as visited
            
            # Recursive calls in all four directions
            dfs(i, j + 1)  # Right
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j - 1)  # Left

        islands = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':  # Found an unvisited island
                    dfs(r, c)  # Start DFS
                    islands += 1  # Increment island count

        return islands
