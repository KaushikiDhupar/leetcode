from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        q=deque()
        old_color=image[sr][sc]
        image[sr][sc]=color

        if old_color==color:
            return image

        q.append([sr,sc])

        while q:
            r,c=q.popleft()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                new_row,new_col=r+dr,c+dc
                if 0 <= new_row < row and 0 <= new_col < col and image[new_row][new_col] == old_color:
                    q.append([new_row,new_col])
                    image[new_row][new_col]=color

        return image




    
        