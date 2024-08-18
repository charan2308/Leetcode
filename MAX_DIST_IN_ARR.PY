class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        mini=arrays[0][0]
        maxi=arrays[0][-1]
        for x in arrays:
            if x[0]<mini:
                mini=x[0]
            if x[-1]>maxi:
                maxi=x[-1]
        
        return abs(maxi-mini)


s=Solution()
print(s.maxDistance([[1,2,3],[4,5],[1,2,3]]))




