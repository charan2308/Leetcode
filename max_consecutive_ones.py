#1004 - max consecutive ones
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # left=0
        # right=0
        # z=0
        # maxi=0
        # cur=0
        # while right<len(nums):
        #     if nums[right]==0:
        #         if z==k:
        #             if nums[left]==0:
        #                 z-=1
        #             left+=1   
        #             continue        
        #         z+=1
        #     cur=right-left+1
        #     maxi=max(maxi,cur) 
        #     right+=1
        # return maxi    
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            print(nums[l:r+1],r-l+1,"k=",k)
        return r-l+1               
            
s=Solution()
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0],3))