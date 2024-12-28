class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # Get grid dimensions

        for i in range(m):  # Loop over rows
            for j in range(n):  # Loop over columns
                if i == j == 0:
                    continue  # Skip the starting cell
                left_path = up_path = float('inf')  # Initialize paths
                if i != 0:  # If not in the first row
                    up_path = grid[i - 1][j] + grid[i][j]
                if j != 0:  # If not in the first column
                    left_path = grid[i][j - 1] + grid[i][j]
                grid[i][j] = min(left_path, up_path)  # Take the minimum path sum

        return grid[m - 1][n - 1]  # Return the minimum path sum to the bottom-right cell
