class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        l=heights.copy()
        l.sort()
        c=0
        for x in range(len(heights)):
           if l[x]!=heights[x]:
               c+=1
        return c
s=Solution()
s.heightChecker([1,4,5,2,3])