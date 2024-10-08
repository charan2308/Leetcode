class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        result=0
        while left<right:
            result = max(result,min(height[left],height[right])*right-left)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        
        return result


s=Solution()
print(s.maxArea([1,2,1]))