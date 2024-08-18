class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elesum=0
        digitsum=0
        for i in nums:
            elesum+=i
            while(i>0):
                digitsum+=i%10
                i=i//10 
        return abs(digitsum-elesum)


s=Solution()
print(s.differenceOfSum([1,15,6,3]))

