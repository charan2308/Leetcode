class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        n=0
        gs=sum(grid[0][:3])
        for x in grid[1:] :
            s=sum(x[:3])
            if s!=gs:
                print(0)
            print(s)

s=Solution()
print(s.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))



