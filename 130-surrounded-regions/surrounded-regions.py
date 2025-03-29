

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # Mark as temporarily safe
            dfs(i, j + 1)  # Right
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i - 1, j)  # Up

        # Step 1: Perform DFS from boundary 'O' cells
        for r in range(m):
            for c in [0, n - 1]:  # First and last column
                if board[r][c] == 'O':
                    dfs(r, c)
        for c in range(n):
            for r in [0, m - 1]:  # First and last row
                if board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Convert remaining 'O' to 'X' (since they are surrounded)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Step 3: Convert 'T' back to 'O' (since they were connected to the boundary)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'T':
                    board[r][c] = 'O'



        """
        Do not return anything, modify board in-place instead.
        """
        