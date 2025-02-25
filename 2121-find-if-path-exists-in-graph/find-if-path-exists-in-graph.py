from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q=deque([source])
        adj_list = {i: [] for i in range(n)}
        visited=set([source])
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        while q:
            node=q.popleft()
            if node==destination :
                return True
            for neighbours in adj_list[node]:
                if neighbours not in visited:
                    q.append(neighbours)
                    visited.add(neighbours)
            
        return False

            


        



        