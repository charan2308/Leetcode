class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        from queue import Queue
        n=len(grid)
        m=len(grid[0])
        queue=Queue()
        visited=[[0]*m for _ in range(n)]
        # print(visited)
        flag1=0
        flag2=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    flag2=1
                    queue.put([[i,j],0])
                    visited[i][j]=2
                elif grid[i][j]==1:
                    flag1=1
                    visited[i][j]=1
        if not flag2:
            if flag1:return -1
            return 0            
        col_change=[1,0,-1,0]
        row_change=[0,1,0,-1]
        print(visited)
        while not queue.empty():
            x = queue.get()
            r=x[0][0]
            c=x[0][1]
            t=x[1]
            for d in range (4) :
                nr=r+row_change[d]
                nc=c+col_change[d]
                if (nr>=0 and nr<n and nc>=0 and nc<m):
                    if visited[nr][nc]==1:
                        visited[nr][nc]=2
                        queue.put([[nr,nc],t+1])
                        # print(nr,nc)
        for x in visited:
            if 1 in x:
                return -1
        return t

s=Solution()
print(s.orangesRotting([[0]]))
        