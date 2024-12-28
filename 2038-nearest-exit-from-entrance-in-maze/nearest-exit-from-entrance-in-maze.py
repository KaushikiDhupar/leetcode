from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        # Directions for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])

        # Queue to store positions in the maze, starting with the entrance
        queue = deque([entrance])
        
        # Mark the entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        steps = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()

                # Check if we are at an exit (but not the entrance)
                if (i != entrance[0] or j != entrance[1]) and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    return steps

                # Explore all possible directions
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj

                    # Check if the new position is within bounds and not visited
                    if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == '.':
                        queue.append((new_i, new_j))
                        maze[new_i][new_j] = '+'  # Mark as visited

            steps += 1

        return -1  # No exit found
