class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        c=0
        for x in range((len(grid))):
            print(x)
            for y in range(len(grid[x])):
                c=0
                if grid[x][y]:
                    c=1
                    if grid[x+1][y]:
                        c+=1
                    if grid[x][y+1]:
                        c+=1
                        print(grid[x][y])
                    
        pass

grid=[[0,1,1,0],[0,1,1,0],[0,0,0,0]]
s=Solution()
print(s.minDays(grid))
