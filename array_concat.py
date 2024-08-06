class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums
s=Solution()
print(s.getConcatenation([1,2,3]))