class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ini_color=image[sr][sc]
        print (ini_color)
        row_change=[0,1,0,-1]
        col_change=[1,0,-1,0]
        m=len(image)
        n=len(image[0])
        def dfs(image,r,c):
            print(r,c)
            
            for i in range(4):
                nr=r+row_change[i]
                nc=c+col_change[i]
                if (nr>=0 and nc>=0 and nr<m and nc<n):
                    print(nr,nc)
                    dfs(image,nr,nc)


        dfs(image,sr,sc)

        pass


s=Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))