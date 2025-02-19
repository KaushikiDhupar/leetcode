from collections import deque
import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        # Priority Queue (Min-Heap) to track minimum effort path
        pq = [(0, 0, 0)]  # (effort, row, col)
        effort_matrix = [[float('inf')] * n for _ in range(m)]
        effort_matrix[0][0] = 0
        
        while pq:
            effort, row, col = heapq.heappop(pq)
            
            # If we reach the bottom-right cell, return the minimum effort
            if row == m - 1 and col == n - 1:
                return effort
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    
                    if new_effort < effort_matrix[new_row][new_col]:
                        effort_matrix[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))

        return -1  # In case there's no valid path (shouldn't happen for a valid grid)
