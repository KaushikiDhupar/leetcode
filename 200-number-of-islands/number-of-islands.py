from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()  # Set to track visited cells
        islands = 0

        # BFS function to explore an island
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # Check all 4 possible directions (up, down, left, right)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (0 <= new_row < rows and 0 <= new_col < cols and  # Ensure within bounds
                        grid[new_row][new_col] == "1" and  # Check if land
                        (new_row, new_col) not in visit):  # Check if unvisited
                        visit.add((new_row, new_col))
                        q.append((new_row, new_col))

        # Iterate through the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:  # Found a new island
                    bfs(r, c)  # Explore the island
                    islands += 1  # Increment island count

        return islands
