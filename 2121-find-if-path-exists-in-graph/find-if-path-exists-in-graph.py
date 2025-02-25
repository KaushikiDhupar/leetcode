from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj_list = {i: [] for i in range(n)}
        visited=set()
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour not in visited and dfs(neighbour):
                    return True
            return False
        return dfs(source)

            


        



        