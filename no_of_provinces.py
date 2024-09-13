class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        graph={}
        n=len(isConnected)
        for a in range(n):
            graph[a]=set()
        for x in range(n):
            for y in range(n):
                if isConnected[x][y] and x!=y:
                    graph[x].add(y)
                    graph[y].add(x)
        print(graph)     
        visited=[0]*n
        count=0
                   
        def dfs(graph,node):
            visited[node]=1
            for x in graph[node]:
                if not visited[x]:
                    dfs(graph,x)
        for x in range(n):
            if not visited[x]:
                count+=1
                dfs(graph,x)
        return count

s=Solution()
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))