class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def dfs(ind,i,j,board,word):
            if ind == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[ind]:
                return False
            temp=board[i][j]
            board[i][j]='#'

            r=[1,0,-1,0]
            c=[0,1,0,-1]
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                if dfs(ind + 1, i + dx, j + dy,board,word):
                    return True
            board[i][j]=temp
            return False
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if dfs(0,i,j,board,word)==True:
                        return True
        return False

